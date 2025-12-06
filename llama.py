import asyncio
from pathlib import Path
import json
from datetime import datetime, timezone
import os
import time

# Third-party imports
from dotenv import load_dotenv
from llama_cloud_services import LlamaParse
import nest_asyncio

# Apply nested asyncio patch (Recommended for SDK internal event loops)
nest_asyncio.apply()

# Load environment variables
load_dotenv()
llama_api_key = os.getenv("LLAMA_CLOUD_API_KEY")

# --- Configuration ---
INPUT_DIR = Path("PDFs")
NUM_WORKERS = 19  # Centralized configuration

# --- Output Configuration ---
BASE_OUTPUT_DIR = Path("llama_parse_results")
MARKDOWNS_DIR = BASE_OUTPUT_DIR / "markdowns"
JSONL_OUTPUT = BASE_OUTPUT_DIR / "results.jsonl"

def get_parser():
    """
    Returns a configured LlamaParse instance using SDK-native concurrency.
    """
    return LlamaParse(
        api_key=llama_api_key,
        num_workers=NUM_WORKERS, 
        parse_mode="parse_page_with_agent",
        model="anthropic-sonnet-4.0",
        high_res_ocr=True, 
        adaptive_long_table=False,
        output_tables_as_HTML=False,
        precise_bounding_box=False,
        page_separator="\n\n---\n\n",
        verbose=False 
    )

def save_results(results, file_paths):
    """
    Process the batch results and save them to disk.
    """
    if not results:
        print("⚠️ No results to save")
        return
    
    timestamp = datetime.now(timezone.utc).isoformat()
    records = []
    
    print(f"💾 Saving {len(results)} results to disk...")

    for i, result in enumerate(results):
        # Validate index bounds
        if i >= len(file_paths):
            print(f"⚠️ Warning: Result index {i} exceeds file_paths length")
            continue
            
        # Map back to original file path (SDK preserves order)
        original_path = Path(file_paths[i])
        
        try:
            # Validate result object
            if result is None:
                raise ValueError("Received None result from parser")
            
            # --- 1. Extract Markdown ---
            # Helper to combine pages into full text
            md_docs = result.get_markdown_documents(split_by_page=True)
            
            if not md_docs:
                print(f"⚠️ Warning: No markdown documents extracted from {original_path.name}")
                full_markdown = ""
            else:
                full_markdown = "\n\n".join([doc.text for doc in md_docs])
            
            # --- 2. Save Markdown File ---
            md_filename = f"{original_path.stem}.md"
            md_path = MARKDOWNS_DIR / md_filename
            
            try:
                md_path.write_text(full_markdown, encoding="utf-8")
            except IOError as e:
                raise IOError(f"Failed to write markdown file: {e}")

            # --- 3. Extract Metadata (Credits, Job ID) ---
            job_metadata = getattr(result, 'job_metadata', {})
            if job_metadata is None:
                job_metadata = {}
                
            credits_used = job_metadata.get('credits_used', 0)
            job_id = getattr(result, 'job_id', "N/A")
            
            # Handle pages count more robustly
            if hasattr(result, 'pages') and result.pages:
                num_pages = len(result.pages)
            elif md_docs:
                num_pages = len(md_docs)
            else:
                num_pages = 0

            # --- 4. Build Record ---
            record = {
                "timestamp": timestamp,
                "service": "llama-cloud",
                "file": str(original_path),
                "filename": original_path.name,
                "job_id": job_id,
                "credits_used": credits_used,
                "pages_processed": num_pages,
                "markdown_file": str(md_path),
                "status": "success"
            }
            records.append(record)
            print(f"✅ Processed: {original_path.name} ({num_pages} pages, {credits_used} credits)")

        except Exception as e:
            print(f"⚠️ Error processing result for {original_path.name}: {e}")
            records.append({
                "timestamp": timestamp,
                "file": str(original_path),
                "filename": original_path.name,
                "error": str(e),
                "status": "failed"
            })

    # --- 5. Write JSONL ---
    try:
        with open(JSONL_OUTPUT, "a", encoding="utf-8") as f:
            for record in records:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
        print(f"📝 Results appended to {JSONL_OUTPUT}")
    except IOError as e:
        print(f"❌ Error writing JSONL file: {e}")

async def main():
    # 1. Validation
    if not llama_api_key:
        print("❌ Error: LLAMA_CLOUD_API_KEY not found in environment variables")
        return
    
    # Get files to parse
    FILES_TO_PARSE = [str(p) for p in INPUT_DIR.glob("*.pdf")]
    
    if not FILES_TO_PARSE:
        print(f"❌ Error: No PDF files found in '{INPUT_DIR}'")
        print(f"   Please ensure the directory exists and contains PDF files")
        return

    # 2. Setup
    try:
        BASE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        MARKDOWNS_DIR.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"❌ Error creating output directories: {e}")
        return
    
    # 3. Execution
    print(f"🚀 Starting LlamaParse Batch (SDK Mode)")
    print(f"📁 Input Directory: {INPUT_DIR}")
    print(f"📄 Files to Process: {len(FILES_TO_PARSE)}")
    print(f"⚙️  Num Workers: {NUM_WORKERS}")
    print(f"📤 Output Directory: {BASE_OUTPUT_DIR}")
    print()
    
    parser = get_parser()
    
    start_time = time.time()
    
    try:
        # --- THE CORE SDK CALL ---
        # We pass the list of strings directly. 
        # The SDK splits this into 'num_workers' concurrent API calls.
        print("⏳ Parsing documents...")
        results = await parser.aparse(FILES_TO_PARSE)
        
        if not results:
            print("⚠️ Warning: Parser returned empty results")
            return
            
    except Exception as e:
        print(f"\n❌ Critical Batch Error: {e}")
        print(f"   Error type: {type(e).__name__}")
        return

    duration = time.time() - start_time
    print(f"\n✅ Batch finished in {duration:.2f} seconds")
    print(f"⏱️  Average time per file: {duration/len(FILES_TO_PARSE):.2f} seconds")

    # 4. Save
    save_results(results, FILES_TO_PARSE)
    
    # 5. Summary Statistics
    if results:
        total_credits = 0
        successful_files = 0
        
        for result in results:
            meta = getattr(result, 'job_metadata', {})
            if meta:
                total_credits += meta.get('credits_used', 0)
                successful_files += 1
        
        print(f"\n📊 Summary:")
        print(f"   Total Files Processed: {successful_files}/{len(FILES_TO_PARSE)}")
        print(f"   Total Credits Used: {total_credits}")
        if successful_files > 0:
            print(f"   Average Credits per File: {total_credits/successful_files:.2f}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⚠️ Process interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print(f"   Error type: {type(e).__name__}")