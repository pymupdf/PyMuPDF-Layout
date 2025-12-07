import os
import time
import requests
from requests.adapters import HTTPAdapter, Retry
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import json
from tqdm import tqdm
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
API_KEY = os.getenv("DATALAB_API_KEY")  # Store API key in environment variable
API_URL = "https://www.datalab.to/api/v1/marker"

MAX_WORKERS = 3  # Number of concurrent conversions
INPUT_DIR = Path("PDFs")
BASE_OUTPUT_DIR = Path("datalab_results")
MARKDOWNS_DIR = BASE_OUTPUT_DIR / "markdowns"
JSONL_OUTPUT = BASE_OUTPUT_DIR / "results.jsonl"

# --- Configure session with retries ---
session = requests.Session()
retries = Retry(
    total=20,
    backoff_factor=4,
    status_forcelist=[429],
    allowed_methods=["GET", "POST"],
    raise_on_status=False,
)
adapter = HTTPAdapter(max_retries=retries)
session.mount("http://", adapter)
session.mount("https://", adapter)


def append_jsonl(record: dict):
    """Append a single JSON record to the JSONL file."""
    with JSONL_OUTPUT.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def submit_and_poll_pdf_conversion(
    pdf_path: Path,
    output_format: str = 'markdown',
    use_llm: bool = True,
    force_ocr: bool = True,
    max_pages: int = None
) -> tuple[Path, bool]:
    """
    Submit PDF for conversion, poll for completion, and save results.
    Returns tuple: (Path, Success_Boolean)
    """
    timestamp = datetime.now(timezone.utc)
    headers = {"X-Api-Key": API_KEY}
    
    try:
        # --- Submit initial request ---
        with open(pdf_path, 'rb') as f:
            form_data = {
                'file': (pdf_path.name, f, 'application/pdf'),
                "force_ocr": (None, force_ocr),
                "paginate": (None, False),
                'output_format': (None, output_format),
                "use_llm": (None, use_llm),
                "strip_existing_ocr": (None, False),
                "disable_image_extraction": (None, False)
            }
            
            if max_pages:
                form_data["max_pages"] = (None, max_pages)
            
            response = session.post(API_URL, headers=headers, files=form_data)
        
        response.raise_for_status()
        data = response.json()
        request_id = data.get("request_id", "unknown")
        
        # --- Poll for completion ---
        check_url = data["request_check_url"]
        max_polls = 300
        poll_interval = 2  # seconds
        
        for i in range(max_polls):
            time.sleep(poll_interval)
            response = session.get(check_url, headers=headers)
            check_result = response.json()
            
            if check_result['status'] == 'complete':
                # --- Extract converted content ---
                converted_document = check_result.get(output_format, "")
                
                # --- Save markdown file ---
                md_filename = f"{pdf_path.stem}.md"
                md_path = MARKDOWNS_DIR / md_filename
                md_path.write_text(converted_document, encoding="utf-8")
                
                # --- Save JSONL record ---
                record = {
                    "timestamp": timestamp.isoformat(),
                    "file": str(pdf_path),
                    "request_id": request_id,
                    "status": "success",
                    "polls_required": i + 1,
                    "markdown_file": str(md_path),
                    "pages_processed": check_result.get("num_pages"),
                    "success": check_result.get("success"),
                }
                append_jsonl(record)
                
                return pdf_path, True  # Success
                
            elif check_result["status"] == "failed":
                # --- Handle failure ---
                error_msg = check_result.get("error", "Unknown error")
                append_jsonl({
                    "timestamp": timestamp.isoformat(),
                    "file": str(pdf_path),
                    "request_id": request_id,
                    "status": "failed",
                    "error": error_msg,
                    "polls_required": i + 1,
                })
                return pdf_path, False  # Failure
        
        # --- Timeout ---
        append_jsonl({
            "timestamp": timestamp.isoformat(),
            "file": str(pdf_path),
            "request_id": request_id,
            "status": "timeout",
            "error": "Polling timeout after max attempts",
        })
        return pdf_path, False  # Failure
        
    except requests.exceptions.RequestException as e:
        append_jsonl({
            "timestamp": timestamp.isoformat(),
            "file": str(pdf_path),
            "error": "request_error",
            "details": str(e),
        })
        return pdf_path, False  # Failure
        
    except Exception as e:
        append_jsonl({
            "timestamp": timestamp.isoformat(),
            "file": str(pdf_path),
            "error": "unexpected_error",
            "details": str(e),
        })
        return pdf_path, False  # Failure


def batch_convert_pdfs():
    """Main function to batch convert all PDFs in the input directory."""
    
    # 1. Create directories
    BASE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    MARKDOWNS_DIR.mkdir(parents=True, exist_ok=True)
    
    # 2. Clear or create the JSONL file
    JSONL_OUTPUT.write_text("")
    
    # 3. Collect all PDF files
    if not INPUT_DIR.exists():
        print(f"Error: Input directory '{INPUT_DIR}' not found!")
        return
    
    docs_to_process = list(INPUT_DIR.glob("*.pdf"))
    
    if not docs_to_process:
        print(f"No PDF files found in '{INPUT_DIR}'")
        return
    
    print(f"Found {len(docs_to_process)} PDFs to convert...")
    print(f"Max concurrent conversions: {MAX_WORKERS}")
    print("=" * 60)
    
    # 4. Process files concurrently with progress bar
    results = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_file = {
            executor.submit(
                submit_and_poll_pdf_conversion,
                pdf_path,
                output_format='markdown',
                use_llm=True,
                force_ocr=True,
                max_pages=None  # Set to 1 or any number to limit pages
            ): pdf_path
            for pdf_path in docs_to_process
        }
        
        # Use tqdm for progress tracking
        with tqdm(total=len(docs_to_process), desc="Converting PDFs") as pbar:
            for future in as_completed(future_to_file):
                pdf_path = future_to_file[future]
                try:
                    path, success = future.result()
                    results.append((path, success))
                    status = "✓" if success else "✗"
                    pbar.set_postfix_str(f"{status} {pdf_path.name}")
                except Exception as e:
                    results.append((pdf_path, False))
                    pbar.set_postfix_str(f"✗ {pdf_path.name}: {e}")
                pbar.update(1)
    
    # 5. Analyze and print summary
    failed_files = [path.name for path, success in results if not success]
    
    print("\n" + "=" * 60)
    print("PROCESSING COMPLETE")
    print("=" * 60)
    print(f"Total Files:  {len(docs_to_process)}")
    print(f"Successful:   {len(docs_to_process) - len(failed_files)}")
    print(f"Failed:       {len(failed_files)}")
    
    if failed_files:
        print("\nFiles that failed:")
        print("-" * 60)
        for fname in failed_files:
            print(f"  ✗ {fname}")
    else:
        print("\n✓ All files processed successfully!")
    
    print("=" * 60)
    print(f"\nResults saved to: {JSONL_OUTPUT}")
    print(f"Markdown files saved to: {MARKDOWNS_DIR}")
    print()


if __name__ == "__main__":
    if not API_KEY:
        print("Error: DATALAB_API_KEY environment variable not set!")
        print("Please set it with: export DATALAB_API_KEY='your-api-key'")
        exit(1)
    
    batch_convert_pdfs()