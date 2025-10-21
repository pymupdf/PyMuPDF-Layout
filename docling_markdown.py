import os
from docling.document_converter import DocumentConverter

# Folder containing PDF files
directory = "PDFs"
# Folder to save markdown output
markdown_folder = "docling_markdowns"

# Make sure output folder exists
os.makedirs(markdown_folder, exist_ok=True)

# List all PDF files in the directory
pdf_files = [f for f in os.listdir(directory) if f.endswith(".pdf")]

# Initialize converter once
converter = DocumentConverter()

for index, pdf in enumerate(pdf_files):
    print(f"Processing {index+1}/{len(pdf_files)}: {pdf}")
    pdf_path = os.path.join(directory, pdf)

    # Output markdown file path
    markdown_output_path = os.path.join(markdown_folder, pdf.replace(".pdf", ".md"))

    # Convert PDF to Docling document
    result = converter.convert(pdf_path)

    # Export to markdown
    md_content = result.document.export_to_markdown()

    # Save markdown
    with open(markdown_output_path, "w", encoding="utf-8") as f:
        f.write(md_content)