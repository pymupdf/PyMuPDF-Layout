# Title: L4-Optimized Docling Pipeline (Reducto-Style Benchmarking)
import os

# --- 1. THREADING LOCK (CRITICAL FOR L4) ---
# Must be set BEFORE importing torch/docling
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["DOCLING_NUM_THREADS"] = "4"


import time
import json
import uuid
import shutil
import logging
import multiprocessing
import gc
import importlib.metadata  # FIX 1: Added missing import
import torch
from pathlib import Path
from datetime import datetime, timezone
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    PdfPipelineOptions,
    AcceleratorOptions,
    AcceleratorDevice,
    RapidOcrOptions,
)
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.utils.model_downloader import download_models

# --- Configuration ---
INPUT_DIR = Path("PDFs")
BASE_OUTPUT_DIR = Path("docling_pipeline_wocr")
MARKDOWNS_DIR = BASE_OUTPUT_DIR / "markdowns"
JSONL_OUTPUT = BASE_OUTPUT_DIR / "results.jsonl"
ARTIFACTS_PATH = Path("models_cache")


# L4 Tuning
NUM_WORKERS = 16  # Optimized for L4 (24GB VRAM) on g2-standard-32
OCR_BATCH_SIZE = 64
LAYOUT_BATCH_SIZE = 32
docling_version = importlib.metadata.version("docling")  # FIX 2: Fixed syntax (added space after =)

# --- Helper: Safe JSONL Writer ---
def append_jsonl_safe(record: dict, lock, file_path: Path):
    """Process-safe append to JSONL."""
    json_line = json.dumps(record, ensure_ascii=False) + "\n"
    with lock:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(json_line)

# --- WORKER FUNCTION ---
def worker_initializer():
    """Clean GPU memory on worker startup."""
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

def _parallel_worker_task(args):
    """
    Worker process:
    1. Loads model ONCE.
    2. Processes a chunk of files.
    3. Writes results safely to shared JSONL.
    """
    file_paths, lock, output_jsonl, output_md_dir = args
    
    # 1. Thread affinity
    torch.set_num_threads(1)
    
    # 2. Configure Pipeline (L4 Optimized)
    accelerator_options = AcceleratorOptions(
        num_threads=4,
        device=AcceleratorDevice.CUDA,
    )
    ocr_options = RapidOcrOptions(backend="torch")
    
    pipeline_options = PdfPipelineOptions(
        artifacts_path=ARTIFACTS_PATH,
        accelerator_options=accelerator_options,
        ocr_options=ocr_options,
        do_ocr=False,
        do_table_structure=False,
        ocr_batch_size=OCR_BATCH_SIZE,
        layout_batch_size=LAYOUT_BATCH_SIZE,
        table_batch_size=16,
        do_formula_enrichment=False,
        do_picture_description=False
    )

    # 3. Initialize Converter
    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(
                pipeline_options=pipeline_options
            )
        }
    )

    success_files = []
    failed_files = []

    # 4. Process Loop
    for i, file_path in enumerate(file_paths):
        start_time = time.time()
        timestamp = datetime.now(timezone.utc)
        file_path = Path(file_path)
        
        try:
            # Conversion
            result = converter.convert(file_path, raises_on_error=True)
            doc = result.document
            duration = time.time() - start_time

            
            # Save Markdown
            md_filename = f"{file_path.stem}.md"
            md_path = output_md_dir / md_filename
            full_markdown = doc.export_to_markdown()
            
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(full_markdown)


            # Create Record (Matching Reducto Schema)
            record = {
                "timestamp": timestamp.isoformat(),
                "docling_version": docling_version,
                "file": str(file_path),
                "duration": duration,
            }
            
            append_jsonl_safe(record, lock, output_jsonl)
            success_files.append(file_path.name)
            print(f"✅ {file_path.name} ({duration:.2f}s)")

            # Memory Hygiene (Flush every 10 files)
            if i % 10 == 0:
                torch.cuda.empty_cache()
                gc.collect()

        except Exception as e:
            # Log Failure
            error_record = {
                "timestamp": timestamp.isoformat(),
                "file": str(file_path),
                "error": "processing_error",
                "details": str(e)
            }
            append_jsonl_safe(error_record, lock, output_jsonl)
            failed_files.append(file_path.name)
            print(f"❌ {file_path.name}: {e}")

    return success_files, failed_files

# --- MAIN LOGIC ---
def main():
    start_global = time.time()
    
    # 1. Setup Directories
    if BASE_OUTPUT_DIR.exists():
        shutil.rmtree(BASE_OUTPUT_DIR)
    BASE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    MARKDOWNS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Initialize empty JSONL
    with open(JSONL_OUTPUT, "w") as f:
        f.write("")

    # 2. Download Models if needed
    if not ARTIFACTS_PATH.exists() or not any(ARTIFACTS_PATH.iterdir()):
        print("📥 Downloading Docling models...")
        download_models(ARTIFACTS_PATH)

    # 3. Prepare Files
    if not INPUT_DIR.exists():
        print(f"❌ Error: Input directory '{INPUT_DIR}' does not exist.")
        return

    all_files = list(INPUT_DIR.glob("*.pdf"))
    if not all_files:
        print(f"No PDF files found in {INPUT_DIR}")
        return

    print(f"🚀 Starting Docling Pipeline on L4 GPU")
    print(f"📂 Files: {len(all_files)}")
    print(f"🤖 Workers: {NUM_WORKERS}")
    
    # 4. Split for Multiprocessing
    # We use a process-safe Manager Lock to allow workers to write to the same JSONL
    manager = multiprocessing.Manager()
    write_lock = manager.Lock()
    
    chunk_size = (len(all_files) + NUM_WORKERS - 1) // NUM_WORKERS
    chunks = [all_files[i:i + chunk_size] for i in range(0, len(all_files), chunk_size)]
    
    # Prepare args for map: (files, lock, jsonl_path, md_dir)
    worker_args = [(chunk, write_lock, JSONL_OUTPUT, MARKDOWNS_DIR) for chunk in chunks]

    # 5. Run Pool
    total_success = []
    total_failed = []
    
    with multiprocessing.get_context("spawn").Pool(
        processes=NUM_WORKERS,
        initializer=worker_initializer
    ) as pool:
        # returns list of (success_list, fail_list) tuples
        results = pool.map(_parallel_worker_task, worker_args)
        
        for success, fail in results:
            total_success.extend(success)
            total_failed.extend(fail)

    # 6. Summary Report (Matching Reducto Style)
    global_duration = time.time() - start_global
    
    print("\n" + "="*40)
    print(f"PROCESSING COMPLETE")
    print("="*40)
    print(f"Total Time:  {global_duration:.2f}s")
    print(f"Total Files: {len(all_files)}")
    print(f"Successful:  {len(total_success)}")
    print(f"Failed:      {len(total_failed)}")
    
    if total_failed:
        print("\nFiles that failed:")
        print("-" * 40)
        for fname in total_failed:
            print(f"❌ {fname}")
    else:
        print("\n✅ All files processed successfully.")
    print("="*40 + "\n")

if __name__ == "__main__":
    main()