import os
import time
from datalab_sdk import ConvertOptions, DatalabClient

# Set your API key
API_KEY = "*"

# Folders
pdf_folder = "PDFs"
markdown_folder = "datalablllm_markdowns"

# Make sure output folder exists
os.makedirs(markdown_folder, exist_ok=True)

# List all PDF files in the directory
pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith(".pdf")]

# Initialize Datalab client
client = DatalabClient(api_key=API_KEY)


options = ConvertOptions(
    # output_format="html",
    max_pages=1,
    force_ocr=True,
    use_llm=True
)

# Determine which files have already been processed
processed_files = set(f.replace(".md", ".pdf") for f in os.listdir(markdown_folder) if f.lower().endswith(".md"))

for index, pdf_file in enumerate(pdf_files):
    if pdf_file in processed_files:
        print(f"Skipping already processed file: {pdf_file}")
        continue

    print(f"Processing {index + 1}/{len(pdf_files)}: {pdf_file}")
    pdf_path = os.path.join(pdf_folder, pdf_file)
    markdown_output_path = os.path.join(markdown_folder, pdf_file.replace(".pdf", ".md"))

    try:
        # Convert PDF to markdown using Datalab
        result = client.convert(pdf_path, options=options)

        # Save markdown content
        with open(markdown_output_path, "w", encoding="utf-8") as f:
            f.write(result.markdown)

        print(f"Saved markdown to {markdown_output_path}")

    except Exception as e:
        print(f"Failed to process {pdf_file}: {e}")

    # Delay 2 seconds before next request
    time.sleep(2)