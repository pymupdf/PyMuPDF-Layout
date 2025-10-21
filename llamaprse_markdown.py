import os
from llama_cloud_services import LlamaParse

# Initialize parser
parser = LlamaParse(
    api_key="*",  # <-- keep key safe in env var
    parse_mode="parse_page_with_agent",
    model="anthropic-sonnet-4.0",
    high_res_ocr=True,
    adaptive_long_table=False,
    outlined_table_extraction=False,
    output_tables_as_HTML=False,
)

# Input & output dirs
directory = "PDFs"
markdown_folder = "llamaparse_highest_markdowns"
os.makedirs(markdown_folder, exist_ok=True)

# Collect all PDFs
pdf_files = [f for f in os.listdir(directory) if f.endswith(".pdf")]

# Get already processed files
processed_files = [f.replace(".md", ".pdf") for f in os.listdir(markdown_folder) if f.endswith(".md")]
skipped_count = 0

for index, pdf in enumerate(pdf_files):
    # Check if already processed
    if pdf in processed_files:
        print(f"Skipping {index+1}/{len(pdf_files)}: {pdf} (already processed)")
        skipped_count += 1
        continue
    
    print(f"Processing {index+1}/{len(pdf_files)}: {pdf}")
    pdf_path = os.path.join(directory, pdf)
    
    try:
        # Parse the file
        result = parser.parse(pdf_path)
        
        # Get markdown docs (split_by_page = True or False, up to you)
        markdown_documents = result.get_markdown_documents(split_by_page=True)
        
        if markdown_documents:  # ensure not empty
            md_text = markdown_documents[0].text  # take only the first
        else:
            md_text = ""
        
        # Save to file
        markdown_output_path = os.path.join(markdown_folder, pdf.replace(".pdf", ".md"))
        with open(markdown_output_path, "w", encoding="utf-8") as f:
            f.write(md_text)
        
        print(f"Saved: {markdown_output_path}")
        
    except Exception as e:
        print(f"Error processing {pdf}: {str(e)}")
        continue

print(f"\nCompleted! Processed {len(pdf_files) - skipped_count} new files, skipped {skipped_count} already processed files.")