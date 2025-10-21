import os
import pymupdf4llm

directory = "PDFs"

pdf_files = [f for f in os.listdir(directory) if f.endswith(".pdf")]

markdown_folder='pymupdf_markdowns'


for index,pdf in enumerate(pdf_files):
    print(f"Processing {index+1}/{len(pdf_files)}: {pdf}")
    pdf_path = os.path.join(directory, pdf)
    #page_127.pdf

    markdown_output_path = os.path.join(markdown_folder, pdf.replace('.pdf', '.md'))
    
    md = pymupdf4llm.to_markdown(pdf_path)
    with open(markdown_output_path, 'w', encoding='utf-8') as f:
        f.write(md)
    