import os
import sys
import time
import logging
import json
import multiprocessing
from pathlib import Path
from typing import Dict, Any
from datetime import datetime, timezone
from importlib.metadata import version

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
INPUT_DIR = Path("PDFs")
MAX_WORKERS = os.cpu_count() or 4  # Utilize all available cores

# Ensure input folder exists
INPUT_DIR.mkdir(parents=True, exist_ok=True)

# Get versions
DOCLING_VERSION = version("docling")
try:
    TORCH_VERSION = version("torch")
except Exception:
    TORCH_VERSION = "N/A"

# -----------------------------------------------------------------------------
# GLOBAL THREADING CONFIGURATION
# -----------------------------------------------------------------------------
# Ideally, these are set before ANY heavy imports (torch, numpy) to take effect.
# We define a helper to set them, but for the main process, they must be set
# before the pool starts. For workers, we set them in the initializer.

def configure_env_for_threading(n_threads: int):
    """
    Sets low-level environment variables to strictly limit thread usage 
    per process. This prevents the 'Oversubscription' performance cliff.
    """
    s_threads = str(n_threads)
    # OpenMP (used by PyTorch/MKL)
    os.environ["OMP_NUM_THREADS"] = s_threads
    # Intel MKL
    os.environ["MKL_NUM_THREADS"] = s_threads
    # OpenBLAS (if MKL is not present)
    os.environ["OPENBLAS_NUM_THREADS"] = s_threads
    # Vector math libraries
    os.environ["VECLIB_MAXIMUM_THREADS"] = s_threads
    os.environ["NUMEXPR_NUM_THREADS"] = s_threads
    # Docling specific (if applicable in future versions)
    os.environ["DOCLING_NUM_THREADS"] = s_threads


def append_jsonl(record: dict, jsonl_output: Path):
    """Append a single JSON record to the JSONL file."""
    with jsonl_output.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


# -----------------------------------------------------------------------------
# LATE IMPORTS
# -----------------------------------------------------------------------------
# We import these inside functions or after env setup to ensure 
# environment variables take precedence over library defaults.

import torch
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import (
    PdfPipelineOptions, 
    AcceleratorOptions, 
    AcceleratorDevice
)
from docling.datamodel.base_models import InputFormat
# Strict No-OCR Backend

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# WORKER PROCESS LOGIC
# -----------------------------------------------------------------------------

def worker_initializer(n_threads: int):
    """
    Called when a new worker process is spawned.
    """
    # 1. Enforce Thread Limits immediately
    configure_env_for_threading(n_threads)
    
    # 2. Force PyTorch to acknowledge the limit
    # (Sometimes Torch ignores env vars if already initialized, so we force it)
    try:
        torch.set_num_threads(n_threads)
    except Exception as e:
        logger.warning(f"Could not enforce torch.set_num_threads: {e}")

def process_single_document(
    file_path: Path, 
    output_dir: Path, 
    do_table_structure: bool,
    do_ocr: bool
) -> Dict[str, Any]:
    """
    The isolated logic for converting one document. 
    This runs inside the worker process.
    """
    file_name = file_path.name
    timestamp = datetime.now(timezone.utc)
    start_time = time.time()
    
    try:
        # ---------------------------------------------------------------------
        # PIPELINE CONFIGURATION (Per-Process)
        # ---------------------------------------------------------------------
        # We re-instantiate options here to ensure no cross-process contamination.
        
        pipeline_options = PdfPipelineOptions()
        
        # OCR SETTINGS - Configurable
        pipeline_options.do_ocr = do_ocr
        pipeline_options.do_code_enrichment = False  # Optimization: Disable if not needed
        pipeline_options.do_formula_enrichment = False # Optimization
        
        # Table Structure: Optional based on user input
        pipeline_options.do_table_structure = do_table_structure
        if do_table_structure:
            # Use text cells from PDF, don't try to OCR the table image
            pipeline_options.table_structure_options.do_cell_matching = True 

        # RESOURCE OPTIMIZATION
        # Disable image generation (huge memory/CPU saver)
        pipeline_options.generate_page_images = False
        pipeline_options.generate_picture_images = False
        
        # ACCELERATOR CONFIGURATION
        # Explicitly set to CPU. 
        # num_threads here informs Docling's internal logic, though OMP_NUM_THREADS
        # handles the heavy lifting of the underlying models.
        pipeline_options.accelerator_options = AcceleratorOptions(
            num_threads=torch.get_num_threads(),
            device=AcceleratorDevice.CPU
        )

        # ---------------------------------------------------------------------
        # CONVERTER INSTANTIATION
        # ---------------------------------------------------------------------
        # We inject the PyPdfiumDocumentBackend to strictly prevent OCR usage.
        
        converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(
                    pipeline_options=pipeline_options,
                    # backend=PyPdfiumDocumentBackend 
                )
            }
        )

        # ---------------------------------------------------------------------
        # CONVERSION & EXPORT
        # ---------------------------------------------------------------------
        
        # Execute conversion
        result = converter.convert(file_path)
        
        # Export to Markdown
        md_content = result.document.export_to_markdown()
        
        # Calculate duration
        duration = time.time() - start_time
        
        # Check if result is empty
        success = bool(md_content and md_content.strip())
        
        # Save markdown file
        md_filename = f"{file_path.stem}.md"
        md_path = output_dir / md_filename
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)

        page_count = len(result.document.pages)
        
        # Create record
        record = {
            "timestamp": timestamp.isoformat(),
            "docling_version": DOCLING_VERSION,
            "torch_version": TORCH_VERSION,
            "file": str(file_path),
            "duration": duration,
            "success": success,
            "pages_processed": page_count,
            "markdown_file": str(md_path),
        }
        
        return record

    except Exception as e:
        duration = time.time() - start_time
        logger.error(f"Failed to process {file_name}: {e}", exc_info=True)
        record = {
            "timestamp": timestamp.isoformat(),
            "docling_version": DOCLING_VERSION,
            "torch_version": TORCH_VERSION,
            "file": str(file_path),
            "duration": duration,
            "success": False,
            "error": "processing_error",
            "details": str(e),
        }
        return record

# -----------------------------------------------------------------------------
# ORCHESTRATION LOGIC
# -----------------------------------------------------------------------------

def run_pipeline(base_output_dir: Path, do_ocr: bool):
    """
    Run the Docling pipeline with specified configuration.
    
    Args:
        base_output_dir: Base directory for output files
        do_ocr: Whether to enable OCR processing
    """
    GLOBAL_START_TIME = time.time()
    
    # Setup output directories
    markdowns_dir = base_output_dir / "markdowns"
    jsonl_output = base_output_dir / "results.jsonl"
    
    base_output_dir.mkdir(parents=True, exist_ok=True)
    markdowns_dir.mkdir(parents=True, exist_ok=True)
    
    # -----------------------------------------------------------------------------
    # CONFIGURATION (Hardcoded)
    # -----------------------------------------------------------------------------
    NUM_WORKERS = 0                  # Number of parallel processes (0 = Auto-calculate)
    THREADS_PER_WORKER = 4           # OpenMP/MKL threads per worker (Recommended: 4-8)
    DISABLE_TABLES = False           # Set to True to disable Table Structure model

    ocr_status = "ENABLED" if do_ocr else "DISABLED"
    print(f"\n--- Initializing Docling CPU Pipeline (OCR: {ocr_status}, CPUs: {MAX_WORKERS}) ---")
    print(f"Docling version: {DOCLING_VERSION}")
    print(f"Torch version: {TORCH_VERSION}")
    print(f"Output directory: {base_output_dir}")

    # Get files
    pdf_files = list(INPUT_DIR.glob("*.pdf"))
    if not pdf_files:
        print(f"No files found in {INPUT_DIR}.")
        return

    print(f"Processing {len(pdf_files)} files...")

    # Clear or create the JSONL file
    jsonl_output.write_text("")

    # Resource Calculation Strategy
    total_physical_cores = multiprocessing.cpu_count()
    
    if NUM_WORKERS > 0:
        num_workers = NUM_WORKERS
    else:
        # Auto-calculation: Total Cores / Threads Per Worker
        calculated = total_physical_cores // THREADS_PER_WORKER
        num_workers = max(1, calculated)
    
    # Safety Check for Oversubscription
    total_projected_threads = num_workers * THREADS_PER_WORKER
    oversubscription_ratio = total_projected_threads / total_physical_cores
    
    print(f"\n{'='*60}")
    print(f"HPC CPU DOCLING PIPELINE CONFIGURATION")
    print(f"{'='*60}")
    print(f"Input Directory      : {INPUT_DIR}")
    print(f"Output Directory     : {base_output_dir}")
    print(f"Total Documents      : {len(pdf_files)}")
    print(f"Physical Cores       : {total_physical_cores}")
    print(f"Worker Processes     : {num_workers}")
    print(f"Threads per Worker   : {THREADS_PER_WORKER}")
    print(f"Total Active Threads : {total_projected_threads}")
    
    if oversubscription_ratio > 1.2:
        print(f"WARNING: Potential Oversubscription (Ratio: {oversubscription_ratio:.2f}x)")
        print(f"         Consider reducing workers or threads per worker.")
    
    print(f"OCR Status           : {ocr_status}")
    print(f"Table Extraction     : {'DISABLED' if DISABLE_TABLES else 'ENABLED'}")
    print(f"{'='*60}\n")

    # Configure the arguments for starmap
    # (file_path, output_dir, do_table_structure, do_ocr)
    tasks = [
        (pdf, markdowns_dir, not DISABLE_TABLES, do_ocr) 
        for pdf in pdf_files
    ]

    # Process files in parallel
    results = []
    
    # Initialize Pool
    # maxtasksperchild=10 is CRITICAL for memory stability.
    # It kills the worker after 10 docs, releasing all RAM.
    with multiprocessing.Pool(
        processes=num_workers,
        initializer=worker_initializer,
        initargs=(THREADS_PER_WORKER,),
        maxtasksperchild=10 
    ) as pool:
        
        try:
            for record in pool.starmap(process_single_document, tasks):
                append_jsonl(record, jsonl_output)
                results.append(record)
                
                # Print status
                if record.get("success"):
                    print(f"✅ {Path(record['file']).name} - {record['duration']:.2f}s")
                else:
                    print(f"❌ {Path(record['file']).name} - {record.get('error', 'unknown error')}")
                
        except KeyboardInterrupt:
            logger.error("\nProcessing interrupted by user. Terminating pool...")
            pool.terminate()
            pool.join()
            sys.exit(1)

    # Print Summary
    successful = sum(1 for r in results if r.get("success"))
    failed = len(results) - successful
    total_duration = sum(r.get("duration", 0) for r in results)
    
    print("\n" + "="*40)
    print(f"PROCESSING COMPLETE (OCR: {ocr_status})")
    print("="*40)
    print(f"Total Files:     {len(pdf_files)}")
    print(f"Successful:      {successful}")
    print(f"Failed:          {failed}")
    print(f"Total Duration:  {total_duration:.2f}s")
    
    if failed > 0:
        print("\nFiles that failed:")
        print("-" * 40)
        for record in results:
            if not record.get("success"):
                print(f"❌ {Path(record['file']).name}")
    else:
        print("\n✅ All files processed successfully.")
    print("="*40 + "\n")

    total_duration = time.time() - GLOBAL_START_TIME
    print(f"Total Duration:  {total_duration:.2f}s")
    
    # Save total duration to file
    duration_file = base_output_dir / "duration.txt"
    with open(duration_file, "w", encoding="utf-8") as f:
        f.write(f"Total Duration: {total_duration:.2f}s\n")
    print(f"Duration saved to: {duration_file}")


def main():
    """Run the pipeline with both OCR and non-OCR configurations."""
    
    # Configuration for both runs
    OCR_OUTPUT_DIR = Path("docling_ocr_results")
    WOCR_OUTPUT_DIR = Path("docling_wocr_results")
    
    print("=" * 60)
    print("RUNNING DOCLING PIPELINE - DUAL MODE")
    print("=" * 60)
    
    # Run 1: With OCR
    print("\n" + "=" * 60)
    print("RUN 1: WITH OCR")
    print("=" * 60)
    run_pipeline(base_output_dir=OCR_OUTPUT_DIR, do_ocr=True)
    
    # Run 2: Without OCR
    print("\n" + "=" * 60)
    print("RUN 2: WITHOUT OCR")
    print("=" * 60)
    run_pipeline(base_output_dir=WOCR_OUTPUT_DIR, do_ocr=False)
    
    print("\n" + "=" * 60)
    print("ALL RUNS COMPLETE")
    print("=" * 60)
    print(f"OCR results saved to: {OCR_OUTPUT_DIR}")
    print(f"Non-OCR results saved to: {WOCR_OUTPUT_DIR}")

if __name__ == "__main__":
    # Force 'spawn' start method - critical for Linux compatibility
    # macOS defaults to 'spawn', but Linux uses 'fork' which causes deadlocks
    # with PyTorch and other threaded libraries
    multiprocessing.set_start_method('spawn', force=True)
    multiprocessing.freeze_support()  # For Windows compatibility
    main()
