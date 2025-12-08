import os
import time
import multiprocessing
import json
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
from importlib.metadata import version

import pymupdf.layout
import pymupdf4llm


# --- Configuration ---
INPUT_DIR = Path("PDFs")
BASE_OUTPUT_DIR = Path("pymupdflayout_results")
MARKDOWNS_DIR = BASE_OUTPUT_DIR / "markdowns"
JSONL_OUTPUT = BASE_OUTPUT_DIR / "results.jsonl"
MAX_WORKERS = os.cpu_count() or 4  # Utilize all available cores

# Ensure folders exist
INPUT_DIR.mkdir(parents=True, exist_ok=True)
BASE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
MARKDOWNS_DIR.mkdir(parents=True, exist_ok=True)

# Get versions
PYMUPDF_VERSION = version("pymupdf")
PYMUPDF4LLM_VERSION = version("pymupdf4llm")
try:
    PYMUPDF_LAYOUT_VERSION = version("pymupdf.layout")
except Exception:
    # If pymupdf.layout is not a separate package
    PYMUPDF_LAYOUT_VERSION = "N/A"


def append_jsonl(record: dict):
    """Append a single JSON record to the JSONL file."""
    with JSONL_OUTPUT.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def convert_single_file(pdf_path: Path) -> dict:
    """
    Worker function: Processes a single PDF file.
    Returns a dict with processing results.
    """
    timestamp = datetime.now(timezone.utc)
    start_time = time.time()
    
    try:
        # Open PDF
        doc = pymupdf.open(pdf_path)
        
        # Get page count before closing
        page_count = doc.page_count
        
        # Convert to Markdown
        md_text = pymupdf4llm.to_markdown(doc)
        
        # Close document
        doc.close()
        
        # Calculate duration
        duration = time.time() - start_time
        
        # Check if result is empty
        success = bool(md_text and md_text.strip())
        
        # Save markdown file
        md_filename = f"{pdf_path.stem}.md"
        md_path = MARKDOWNS_DIR / md_filename
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_text)
        
        # Create record
        record = {
            "timestamp": timestamp.isoformat(),
            "pymupdf_version": PYMUPDF_VERSION,
            "pymupdf4llm_version": PYMUPDF4LLM_VERSION,
            "pymupdf_layout_version": PYMUPDF_LAYOUT_VERSION,
            "file": str(pdf_path),
            "duration": duration,
            "success": success,
            "pages_processed": page_count,
            "markdown_file": str(md_path),
        }
        
        return record
        
    except Exception as e:
        duration = time.time() - start_time
        record = {
            "timestamp": timestamp.isoformat(),
            "pymupdf_version": PYMUPDF_VERSION,
            "pymupdf4llm_version": PYMUPDF4LLM_VERSION,
            "pymupdf_layout_version": PYMUPDF_LAYOUT_VERSION,
            "file": str(pdf_path),
            "duration": duration,
            "success": False,
            "error": "processing_error",
            "details": str(e),
        }
        return record


def main():
    GLOBAL_START_TIME = time.time() 
    print(f"--- Initializing PyMuPDF Pipeline (CPUs: {MAX_WORKERS}) ---")
    print(f"PyMuPDF version: {PYMUPDF_VERSION}")
    print(f"PyMuPDF4LLM version: {PYMUPDF4LLM_VERSION}")
    print(f"PyMuPDF Layout version: {PYMUPDF_LAYOUT_VERSION}")

    # Get files
    pdf_files = list(INPUT_DIR.glob("*.pdf"))
    if not pdf_files:
        print(f"No files found in {INPUT_DIR}.")
        return

    print(f"Processing {len(pdf_files)} files...")

    # Clear or create the JSONL file
    JSONL_OUTPUT.write_text("")

    # Process files in parallel
    results = []
    with ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # Submit all tasks
        futures = {executor.submit(convert_single_file, pdf): pdf for pdf in pdf_files}
        
        # Process results as they finish
        for future in as_completed(futures):
            record = future.result()
            append_jsonl(record)
            results.append(record)
            
            # Print status
            if record.get("success"):
                print(f"✅ {Path(record['file']).name} - {record['duration']:.2f}s")
            else:
                print(f"❌ {Path(record['file']).name} - {record.get('error', 'unknown error')}")

    # Print Summary
    successful = sum(1 for r in results if r.get("success"))
    failed = len(results) - successful
    total_duration = sum(r.get("duration", 0) for r in results)
    
    print("\n" + "="*40)
    print(f"PROCESSING COMPLETE")
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


if __name__ == "__main__":
    # Windows requires this protection for multiprocessing
    multiprocessing.freeze_support() 
    main()