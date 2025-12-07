import asyncio
from pathlib import Path
import json
from datetime import datetime, timezone
import os
import time

# Third-party imports
from dotenv import load_dotenv
from llama_cloud_services import LlamaParse


# Load environment variables
load_dotenv()
llama_api_key = os.getenv("LLAMA_CLOUD_API_KEY")

# --- Configuration ---
INPUT_DIR = Path("PDFs")
NUM_WORKERS = 19
BASE_OUTPUT_DIR = Path("llama_parse_results")
MARKDOWNS_DIR = BASE_OUTPUT_DIR / "markdowns"
JSONL_OUTPUT = BASE_OUTPUT_DIR / "results.jsonl"

# --- Model & Cost Configuration ---
# 1. Define your models and their costs here
MODEL_COSTS = {
    "anthropic-sonnet-4.5": 90,
    "gpt-4o": 7,
    "gpt-4o-mini": 2,
    "llama-3.2-90b": 4
}

# 2. Select the model you want to use
SELECTED_MODEL = "anthropic-sonnet-4.5"

def get_parser():
    """
    Returns a configured LlamaParse instance using the SELECTED_MODEL.
    """
    print(f"ℹ️  Initializing parser with model: {SELECTED_MODEL}")
    return LlamaParse(
        api_key=llama_api_key,
        num_workers=NUM_WORKERS, 
        parse_mode="parse_page_with_agent",
        model=SELECTED_MODEL,  # Uses the variable defined above
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
    Returns the count of successfully extracted files.
    """
    if not results:
        print("⚠️ No results to save")
        return 0
    
    timestamp = datetime.now(timezone.utc).isoformat()
    records = []
    successfully_extracted = 0
    
    # Get the fixed credit cost from the dictionary
    model_credit_cost = MODEL_COSTS.get(SELECTED_MODEL, 0)
    
    print(f"💾 Saving {len(results)} results to disk...")

    for i, result in enumerate(results):
        # Validate index bounds
        if i >= len(file_paths):
            print(f"⚠️ Warning: Result index {i} exceeds file_paths length")
            continue
            
        # Map back to original file path
        original_path = Path(file_paths[i])
        
        try:
            # Validate result object
            if result is None:
                raise ValueError("Received None result from parser")
            
            # --- 1. Extract Markdown ---
            md_docs = result.get_markdown_documents(split_by_page=True)
            
            full_markdown = ""
            parsing_error = None
            
            if not md_docs:
                parsing_error = "No markdown documents extracted"
                print(f"⚠️ Warning: No markdown content for {original_path.name}")
            else:
                full_markdown = "\n\n".join([doc.text for doc in md_docs])
                # Double check if text is empty string
                if not full_markdown.strip():
                    parsing_error = "Extracted markdown is empty"

            # --- 2. Save Markdown File (Only if we have content) ---
            md_filename = f"{original_path.stem}.md"
            md_path = MARKDOWNS_DIR / md_filename
            
            try:
                md_path.write_text(full_markdown, encoding="utf-8")
            except IOError as e:
                raise IOError(f"Failed to write markdown file: {e}")

            # --- 3. Extract Metadata (Credits from Dict, ID from Result) ---
            job_id = getattr(result, 'job_id', "N/A")
            credits_used = model_credit_cost # Uses dictionary value
            
            if hasattr(result, 'pages') and result.pages:
                num_pages = len(result.pages)
            elif md_docs:
                num_pages = len(md_docs)
            else:
                num_pages = 0

            # --- 4. Determine Status & Build Record ---
            if parsing_error:
                status = "failed"
                record_error = parsing_error
            else:
                status = "success"
                record_error = None
                successfully_extracted += 1 

            record = {
                "timestamp": timestamp,
                "service": "llama-cloud",
                "model": SELECTED_MODEL,
                "file": str(original_path),
                "filename": original_path.name,
                "job_id": job_id,
                "markdown_file": str(md_path),
                "status": status,
                "credits_used": credits_used,
                "pages": num_pages
            }
            
            if record_error:
                record["error"] = record_error

            records.append(record)
            
            if status == "success":
                print(f"✅ Processed: {original_path.name} ({num_pages} pages, {credits_used} credits)")
            else:
                print(f"⚠️ Failed Logic: {original_path.name} - {record_error}")

        except Exception as e:
            print(f"❌ Error processing result for {original_path.name}: {e}")
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
    
    return successfully_extracted

async def main():
    # 1. Validation
    if not llama_api_key:
        print("❌ Error: LLAMA_CLOUD_API_KEY not found in environment variables")
        return

    # Validate Dictionary Config
    if SELECTED_MODEL not in MODEL_COSTS:
        print(f"⚠️ Warning: Model '{SELECTED_MODEL}' not found in MODEL_COSTS dictionary.")
        print("   Credits will be recorded as 0.")
    
    FILES_TO_PARSE = [str(p) for p in INPUT_DIR.glob("*.pdf")]
    
    if not FILES_TO_PARSE:
        print(f"❌ Error: No PDF files found in '{INPUT_DIR}'")
        return

    # 2. Setup
    try:
        BASE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        MARKDOWNS_DIR.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"❌ Error creating output directories: {e}")
        return
    
    # 3. Execution
    print(f"🚀 Starting LlamaParse Batch")
    print(f"🤖 Model: {SELECTED_MODEL}")
    print(f"💰 Cost per file: {MODEL_COSTS.get(SELECTED_MODEL, 'Unknown')}")
    print(f"📄 Files to Process: {len(FILES_TO_PARSE)}")
    print(f"⚙️  Num Workers: {NUM_WORKERS}")
    
    parser = get_parser()
    
    start_time = time.time()
    
    try:
        print("⏳ Parsing documents...")
        results = await parser.aparse(FILES_TO_PARSE)
        
        if not results:
            print("⚠️ Warning: Parser returned empty results")
            return
            
    except Exception as e:
        print(f"\n❌ Critical Batch Error: {e}")
        return

    duration = time.time() - start_time
    print(f"\n✅ Batch finished in {duration:.2f} seconds")

    # 4. Save and get success count
    successfully_extracted_count = save_results(results, FILES_TO_PARSE)
    
    # 5. Summary Statistics
    if results:
        # Calculate total credits based on dictionary logic
        cost_per_file = MODEL_COSTS.get(SELECTED_MODEL, 0)
        total_credits = len(results) * cost_per_file
        
        print(f"\n📊 Summary:")
        print(f"   Total Files Processed: {successfully_extracted_count}/{len(FILES_TO_PARSE)}")
        print(f"   Total Credits Used: {total_credits}")
        print(f"   (Based on fixed cost: {cost_per_file} credits/file for {SELECTED_MODEL})")
    
    print(f"\n🎯 Total files extracted correctly: {successfully_extracted_count}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⚠️ Process interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")