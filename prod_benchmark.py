
import json
import pandas as pd
from utils import find_best_match_and_normalized_distance

# =============================================================================
# CONFIGURATION
# =============================================================================

# --- Input Files ---
GROUND_TRUTH_FILE = "cleaned_output.json"
PAGE_MAPPING_FILE = "page_folder_mapping.csv"

# --- Output File ---
OUTPUT_CSV_FILE = "benchmark_results_final.csv"

# --- Method Definitions ---
# Each tuple contains: (folder_name, column_name_for_results)
FOLDER_INFO = [
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

# --- Analysis Parameters ---
# Rows where the best score across all methods is not below this threshold will be excluded.
# A lower score (distance) is better.
MIN_SCORE_THRESHOLD = 0.25
# Folders from the mapping file to exclude from the final analysis.
EXCLUDED_FOLDERS = ["test"]

# Automatically derive the list of score columns from FOLDER_INFO
SCORE_COLUMNS = [col_name for _, col_name in FOLDER_INFO]


def generate_raw_scores(ground_truth_data: list, folder_info: list) -> pd.DataFrame:
    """
    Processes ground truth data against markdown files from various methods.

    For each piece of text ("needle") in the ground truth, this function searches
    for the best match in the corresponding page's markdown file ("haystack")
    for each specified method.

    Args:
        ground_truth_data: A list of dictionaries, where each dictionary
                           represents a page and contains its 'page_number'
                           and a list of 'texts' to find.
        folder_info: A list of tuples, each defining a method's folder
                     and the desired column name for its scores.

    Returns:
        A pandas DataFrame containing the raw scores (normalized distances)
        for each needle against each method.
    """
    all_results = []
    total_entries = len(ground_truth_data)

    print("Generating raw scores...")
    for index, ground_truth_entry in enumerate(ground_truth_data):
        print(f"Processing page group {index + 1}/{total_entries}")
        page_number = ground_truth_entry['page_number']

        for needle_index, needle_text in enumerate(ground_truth_entry['texts']):
            row = {
                'page_number': page_number,
                'needle_index': needle_index,
                'needle': needle_text
            }

            for folder_name, col_name in folder_info:
                markdown_path = f"{folder_name}/page_{page_number}.md"
                try:
                    with open(markdown_path, 'r', encoding='utf-8') as f:
                        md_content = f.read()
                    
                    # The score is the normalized distance; lower is better.
                    _, score = find_best_match_and_normalized_distance(needle_text, md_content)
                except FileNotFoundError:
                    score = None
                
                row[col_name] = score
            
            all_results.append(row)

    return pd.DataFrame(all_results)


def analyze_results(scores_df: pd.DataFrame, mapping_file: str) -> pd.DataFrame:
    """
    Analyzes the raw scores to produce a final summary report.

    This function merges scores with page-folder mappings, filters data,
    calculates mean accuracy, adds folder counts, computes a weighted
    average, and sorts the results for presentation.

    Args:
        scores_df: DataFrame with raw scores from generate_raw_scores.
        mapping_file: Path to the CSV file mapping page numbers to folders.

    Returns:
        A pandas DataFrame containing the final, formatted benchmark results.
    """
    print("\nAnalyzing results...")
    
    # 1. Merge with page-folder mapping
    page_mapping_df = pd.read_csv(mapping_file)
    merged_df = scores_df.merge(page_mapping_df, left_on="page_number", right_on="Page")

    # 2. Filter data
    # Drop rows where any method failed to produce a score
    filtered_df = merged_df.dropna(subset=SCORE_COLUMNS).copy()
    # Exclude specified folders (e.g., 'test' folders)
    filtered_df = filtered_df[~filtered_df["Folder"].isin(EXCLUDED_FOLDERS)]
    # Keep only rows where at least one method found a close match
    filtered_df = filtered_df[filtered_df[SCORE_COLUMNS].min(axis=1) < MIN_SCORE_THRESHOLD]

    if filtered_df.empty:
        print("Warning: No data left after filtering. Cannot generate report.")
        return pd.DataFrame()

    # 3. Calculate mean scores (distances) grouped by folder type
    mean_distances = filtered_df.groupby("Folder")[SCORE_COLUMNS].mean()
    
    # 4. Convert distance to accuracy percentage and add folder counts
    # Accuracy = (1 - distance) * 100
    final_report = ((1 - mean_distances) * 100).round(2)
    folder_counts = filtered_df.groupby("Folder").size()
    final_report['Folder_Count'] = folder_counts.astype(int)

    # 5. Calculate and append a weighted mean row
    total_count = folder_counts.sum()
    weighted_means = {}
    for col in SCORE_COLUMNS:
        weighted_mean_distance = (mean_distances[col] * folder_counts).sum() / total_count
        weighted_mean_accuracy = ((1 - weighted_mean_distance) * 100).round(2)
        weighted_means[col] = weighted_mean_accuracy
        
    weighted_mean_row = pd.Series(weighted_means, name='Weighted_Mean')
    weighted_mean_row['Folder_Count'] = int(total_count)
    final_report = pd.concat([final_report, weighted_mean_row.to_frame().T])

    # 6. Sort columns by performance (descending weighted mean accuracy)
    weighted_accuracies = final_report.loc['Weighted_Mean', SCORE_COLUMNS]
    sorted_cols = weighted_accuracies.sort_values(ascending=False).index.tolist()
    final_report = final_report[sorted_cols + ['Folder_Count']]

    return final_report


def main():
    """Main function to run the entire benchmarking process."""
    
    # Load ground truth data
    try:
        with open(GROUND_TRUTH_FILE) as f:
            cleaned_full_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Ground truth file not found at '{GROUND_TRUTH_FILE}'")
        return

    # Step 1: Generate raw scores for all methods
    raw_scores_df = generate_raw_scores(cleaned_full_data, FOLDER_INFO)

    # Step 2: Analyze scores and create the final report
    final_result_df = analyze_results(raw_scores_df, PAGE_MAPPING_FILE)

    # Step 3: Save the report to a CSV file
    if not final_result_df.empty:
        final_result_df.to_csv(OUTPUT_CSV_FILE)
        print("\n" + "="*50)
        print("ANALYSIS COMPLETE")
        print("="*50)
        print(f"Final results saved to: {OUTPUT_CSV_FILE}")
        print("\nFinal Report:")
        print(final_result_df)


if __name__ == "__main__":
    main()