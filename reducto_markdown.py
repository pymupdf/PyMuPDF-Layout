import asyncio
from pathlib import Path
import json
from datetime import datetime, timezone
from reducto import (
    AsyncReducto,
    APIConnectionError,
    RateLimitError,
    APIStatusError,
    __version__ as reducto_version
)
from dotenv import load_dotenv
from tqdm.asyncio import tqdm
import os

load_dotenv()
reducto_api_key = os.getenv("REDUCTO_API_KEY")

client = AsyncReducto(api_key=reducto_api_key)

MAX_CONCURRENCY = 30
INPUT_DIR = Path("PDFs")
FILES_TO_PARSE = list(INPUT_DIR.glob("*.pdf"))

# --- Configuration for Output folders ---
BASE_OUTPUT_DIR = Path("reducto")
MARKDOWNS_DIR = BASE_OUTPUT_DIR / "markdowns"
JSONL_OUTPUT = BASE_OUTPUT_DIR / "results.jsonl"


async def append_jsonl(record: dict):
    """Append a single JSON record to the JSONL file."""
    with JSONL_OUTPUT.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


async def parse_document(path: Path, sem: asyncio.Semaphore) -> tuple[Path, bool]:
    """
    Parses a document and returns a tuple: (Path, Success_Boolean).
    Returns True if successful (200 OK), False otherwise.
    """
    async with sem:
        timestamp = datetime.now(timezone.utc)

        try:
            upload = await client.upload(file=path)
            result = await client.parse.run(
                input=upload,
                formatting={"table_output_format": "md"}
            )

            # ---------- FULL MARKDOWN ----------
            full_markdown = "\n\n".join(
                chunk.content for chunk in result.result.chunks
            )

            # ---------- SAVE MARKDOWN FILE ----------
            md_filename = f"{path.stem}.md"
            md_path = MARKDOWNS_DIR / md_filename
            md_path.write_text(full_markdown, encoding="utf-8")

            # ---------- JSONL RECORD ----------
            record = {
                "timestamp": timestamp.isoformat(),
                "reducto_version": reducto_version,
                "file": str(path),
                "job_id": result.job_id,
                "duration": result.duration,
                "credits_used": result.usage.credits,
                "pages_processed": result.usage.num_pages,
                "studio_link": result.studio_link,
                "markdown_file": str(md_path),
                "full_result": result.model_dump(),
            }

            await append_jsonl(record)
            return path, True # Success

        except APIConnectionError as e:
            await append_jsonl({
                "timestamp": timestamp.isoformat(),
                "reducto_version": reducto_version,
                "file": str(path),
                "error": "connection_error",
                "details": str(e),
            })
            return path, False # Failure

        except RateLimitError:
            await append_jsonl({
                "timestamp": timestamp.isoformat(),
                "reducto_version": reducto_version,
                "file": str(path),
                "error": "rate_limit",
            })
            return path, False # Failure

        except APIStatusError as e:
            await append_jsonl({
                "timestamp": timestamp.isoformat(),
                "reducto_version": reducto_version,
                "file": str(path),
                "error": "api_status",
                "status_code": e.status_code,
                "response": str(e.response),
            })
            return path, False # Failure

        except Exception as e:
            # Catch-all for other unexpected errors (file read, etc.)
            await append_jsonl({
                "timestamp": timestamp.isoformat(),
                "reducto_version": reducto_version,
                "file": str(path),
                "error": "unexpected_error",
                "details": str(e),
            })
            return path, False # Failure


async def main():
    # 1. Create directories
    BASE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    MARKDOWNS_DIR.mkdir(parents=True, exist_ok=True)

    # 2. Clear or create the JSONL file
    JSONL_OUTPUT.write_text("")

    sem = asyncio.Semaphore(MAX_CONCURRENCY)

    # 3. Run and gather results
    results = await tqdm.gather(
        *[parse_document(path, sem) for path in FILES_TO_PARSE],
        desc="Parsing PDFs"
    )

    # 4. Analyze failures
    # results is a list of tuples: [(path, is_success), ...]
    failed_files = [path.name for path, success in results if not success]
    
    # 5. Print Summary
    print("\n" + "="*40)
    print(f"PROCESSING COMPLETE")
    print("="*40)
    print(f"Total Files: {len(FILES_TO_PARSE)}")
    print(f"Successful:  {len(FILES_TO_PARSE) - len(failed_files)}")
    print(f"Failed:      {len(failed_files)}")
    
    if failed_files:
        print("\nFiles that failed (did not get 200 OK):")
        print("-" * 40)
        for fname in failed_files:
            print(f"❌ {fname}")
    else:
        print("\n✅ All files processed successfully.")
    print("="*40 + "\n")


if __name__ == "__main__":
    asyncio.run(main())