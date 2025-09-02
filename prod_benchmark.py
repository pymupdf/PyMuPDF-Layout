import pandas as pd



import json
from rapidfuzz import fuzz, distance

def find_best_match_and_normalized_distance(needle: str, haystack: str):
    """
    Finds the best fuzzy match of a needle in a haystack and returns
    the matched text and its _normalized_ Levenshtein distance.
    Args:
        needle: The string to search for (ground truth).
        haystack: The string to search within
    
    Returns:
        A tuple containing (best_matched_substring, normalized_levenshtein_distance),
        or (None, None) if no plausible match is found.
    """
    if not needle or not haystack:
        return None, None
    
    # 1. Directly find the alignment of the best partial match.
    alignment = fuzz.partial_ratio_alignment(needle, haystack)
    
    if alignment is None:
        return None, None
    
    # 2. Extract the best matching substring using the alignment indices.
    best_match_str = haystack[alignment.dest_start : alignment.dest_end]
    
    # 3. Calculate the raw Levenshtein distance.
    raw_dist = distance.Levenshtein.distance(needle, best_match_str)
    
    # 4. Normalize the distance.
    # Get the length of the longer string.
    max_len = max(len(needle), len(best_match_str))
    
    # Divide the raw distance by the max length, handling the case of empty strings.
    normalized_dist = raw_dist / max_len if max_len > 0 else 0.0
    
    return best_match_str, normalized_dist

# Define folder names and their corresponding column names
folder_info = [
    ('reducto_markdowns', 'reducto'),
    ('pymupdf_markdowns', 'pymupdf'),
    ('llamaparse_markdowns', 'llamaparse'),
    ('datalab_markdowns', 'datalab'),
    ('gemini_markdowns', 'gemini'),
    ('docling_markdowns', 'docling'),
    ('geminipro_markdowns', 'geminipro'),
    ('llamaparse_highest_markdowns', 'llamaparse_highest'),
    ('datalablllm_markdowns', 'datalabllm')

]

# Load ground truth data once
with open("cleaned_output.json") as f:
    cleaned_full_data = json.load(f)

# Initialize results dictionary
all_results = []

# Process all ground truth entries
for index, ground in enumerate(cleaned_full_data):
    print(f"Processing {index+1}/{len(cleaned_full_data)}")
    page_number = ground['page_number']
    # Process each needle text with its index
    for needle_index, needle in enumerate(ground['texts']):
        row = {
            'page_number': page_number,
            'needle_index': needle_index,  # Add the array location
            'needle': needle
        }
        # Get scores from each folder
        for folder_name, col_name in folder_info:
            markdown_path = f"{folder_name}/page_{page_number}.md"
            try:
                with open(markdown_path, 'r', encoding='utf-8') as f:
                    md_content = f.read()
                match_result = find_best_match_and_normalized_distance(needle, md_content)
                score = match_result[1]  # Assuming this is the distance/score
            except FileNotFoundError:
                score = None  # or use np.nan
            row[col_name] = score
        all_results.append(row)

# Create DataFrame
df = pd.DataFrame(all_results)

# Calculate means for each method
print("\n" + "="*50)
print("MEAN SCORES BY METHOD:")
print("="*50)
score_columns = [col_name for _, col_name in folder_info]
# Save complete results
num_cols = ["reducto", "pymupdf", "llamaparse", "datalab","datalabllm",
             "gemini", "docling", "geminipro","llamaparse_highest"]
df = df.dropna(subset=num_cols)
map = pd.read_csv("page_folder_mapping.csv")
dm = df.merge(map, left_on="page_number", right_on="Page")  
dm = dm[dm["Folder"] != "test"]
dm = dm[dm[num_cols].min(axis=1) < 0.25]
result = dm.groupby("Folder")[num_cols].mean()
final_result = ((1 - result) * 100).round(2)

# Add folder count column as integer
folder_counts = dm.groupby("Folder").size().astype(int)
final_result['Folder_Count'] = folder_counts

# Calculate weighted mean for each column
weighted_means = {}
for col in num_cols:
    # Calculate weighted mean: sum(value * weight) / sum(weights)
    weighted_mean = (result[col] * folder_counts).sum() / folder_counts.sum()
    weighted_mean_percentage = ((1 - weighted_mean) * 100).round(2)
    weighted_means[col] = weighted_mean_percentage

# Add weighted mean as a new row
weighted_mean_row = pd.Series(weighted_means, name='Weighted_Mean')
weighted_mean_row['Folder_Count'] = int(folder_counts.sum())  # Ensure it's an integer

# Append weighted mean row to the final result
final_result = pd.concat([final_result, weighted_mean_row.to_frame().T])

# Convert Folder_Count to integer type to ensure proper formatting
final_result['Folder_Count'] = final_result['Folder_Count'].astype(int)

# Get the order of columns based on weighted mean (excluding Folder_Count)
weighted_mean_values = final_result.loc['Weighted_Mean', num_cols]
sorted_cols = weighted_mean_values.sort_values(ascending=False).index.tolist()

# Reorder columns: sorted method columns + Folder_Count at the end
final_result = final_result[sorted_cols + ['Folder_Count']]

# Display the final result
final_result.to_csv('benchmark_results_final.csv')