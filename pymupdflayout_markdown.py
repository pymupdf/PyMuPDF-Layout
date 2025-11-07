import pymupdf.layout
pymupdf.layout.activate()
import pymupdf4llm
import os

directory = "PDFs"

pdf_files = [f for f in os.listdir(directory) if f.endswith(".pdf")]

markdown_folder='pymupdflayout_markdowns'


for index,pdf in enumerate(pdf_files):
    print(f"Processing {index+1}/{len(pdf_files)}: {pdf}")
    pdf_path = os.path.join(directory, pdf)
    #page_127.pdf

    markdown_output_path = os.path.join(markdown_folder, pdf.replace('.pdf', '.md'))
    doc = pymupdf.open(pdf_path)
    md = pymupdf4llm.to_markdown(doc)
    with open(markdown_output_path, 'w', encoding='utf-8') as f:
        f.write(md)
    