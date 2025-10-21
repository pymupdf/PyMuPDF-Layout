import os
import time
from pathlib import Path
from google import genai

client=genai.Client(api_key="*")  # <-- keep key safe in env var


# 2. Define Folders
pdf_folder = Path("PDFs")
markdown_folder = Path("geminipro_markdowns") # Changed folder name to avoid mixing results
markdown_folder.mkdir(exist_ok=True)



# 4. Define the Master Prompt for conversion
with open("ai_prompt.md", "r") as f:
    MASTER_PROMPT = f.read()


# 5. List all PDFs
pdf_files = [f for f in pdf_folder.glob("*.pdf")]
# Determine which files have already been processed
processed_files = set(f.stem + ".pdf" for f in markdown_folder.glob("*.md"))

for index, pdf_file in enumerate(pdf_files):
    if pdf_file.name in processed_files:
        print(f"Skipping already processed file: {pdf_file.name}")
        continue

    print(f"Processing {index + 1}/{len(pdf_files)}: {pdf_file.name}")

    # Upload PDF

    sample_pdf = client.files.upload(file=str(pdf_file))

    response = client.models.generate_content(
    model="gemini-2.5-pro",
    contents=[MASTER_PROMPT, sample_pdf],
)
    with open(markdown_folder / f"{pdf_file.stem}.md", "w", encoding="utf-8") as f:

        if response.text is None:
            print(f"No response text for {pdf_file.name}, skipping.")
            continue
        f.write(response.text)


   