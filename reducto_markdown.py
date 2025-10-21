import time
from pathlib import Path
from reducto import Reducto

# Folders
pdf_folder = Path("PDFs")
markdown_folder = Path("reducto_markdowns")
markdown_folder.mkdir(exist_ok=True)

# Initialize Reducto client
client = Reducto(
    api_key="*",
    environment="production"
    )

# List all PDFs
pdf_files = [f for f in pdf_folder.glob("*.pdf")]

# Determine which files have already been processed
processed_files = set(f.stem + ".pdf" for f in markdown_folder.glob("*.md"))

for index, pdf_file in enumerate(pdf_files):
    if pdf_file.name in processed_files:
        print(f"Skipping already processed file: {pdf_file.name}")
        continue

    print(f"Processing {index + 1}/{len(pdf_files)}: {pdf_file.name}")

    try:
        # Upload PDF
        upload_url = client.upload(file=pdf_file)

        # Parsing options
        options = {
            "ocr_mode": "agentic",
            "chunking": {
        "chunk_mode": "disabled"
            },
            "table_summary": {"enabled": True, "prompt": ""},
            "figure_summary": {"enabled": True, "prompt": "", "override": False}
        }

        advanced_options = {
            "ocr_system": "multilingual",
            "table_output_format": "md",
            "keep_line_breaks": True,
            "persist_results": True,
            "page_range": {"start": 1, "end": 2}  # process all pages if end=None
        }

        experimental_options = {}

        # Run parsing
        result = client.parse.run(
            document_url=upload_url,
            options=options,
            advanced_options=advanced_options,
            experimental_options=experimental_options
        )

        r=result.result.chunks[0].content

        # Save result to markdown
        markdown_output_path = markdown_folder / (pdf_file.stem + ".md")
        with open(markdown_output_path, "w", encoding="utf-8") as f:
            f.write(r)

        print(f"Saved markdown to {markdown_output_path}")

    except Exception as e:
        print(f"Failed to process {pdf_file.name}: {e}")

    # Delay 2 seconds before next request
    time.sleep(2)