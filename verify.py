import os

folders = [
    'datalab_results',
    'pymupdflayout_results',
    'gemini_results',
    'llama_parse_results',
    'reducto_results',
    'docling_results'
]

# Dictionary to keep count of missing or empty files per folder
missing_counts = {}

for folder in folders:
    missing_counts[folder] = 0  # Initialize count
    
    if not os.path.isdir(folder):
        print(f"Missing top-level folder: {folder}")
        missing_counts[folder] = 'Folder missing'
        continue  # Skip further checks if top-level folder is missing

    markdowns_path = os.path.join(folder, 'markdowns')
    if not os.path.isdir(markdowns_path):
        print(f"Missing 'markdowns' folder in {folder}")
        missing_counts[folder] = 'Markdowns folder missing'
        continue

    # Check files page_1.md to page_129.md
    for i in range(1, 130):
        file_name = f"page_{i}.md"
        file_path = os.path.join(markdowns_path, file_name)
        if not os.path.isfile(file_path):
            print(f"Missing file: {file_path}")
            missing_counts[folder] += 1
        else:
            if os.path.getsize(file_path) == 0:
                print(f"Empty file: {file_path}")
                missing_counts[folder] += 1

# Summary of missing/empty files
print("\nSummary of missing/empty markdown files:")
for folder, count in missing_counts.items():
    print(f"{folder}: {count}")