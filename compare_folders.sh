#!/bin/bash

# Script to compare files between two folders
# Usage: compare_folders.sh <folder1> <folder2> [output_file]
# e.g.: compare_folders.sh pymupdf_markdowns pymupdflayout_markdowns differences.txt

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if git is available
if ! command -v git &> /dev/null; then
    echo "ERROR: Git is not installed or not in PATH"
    echo "Please install git first"
    exit 1
fi

# Check arguments
if [ $# -lt 2 ]; then
    echo "Usage: $0 <folder1> <folder2> [output_file]"
    echo ""
    echo "Example: $0 /path/to/version1 /path/to/version2"
    echo "Example: $0 /path/to/version1 /path/to/version2 differences.txt"
    exit 1
fi

FOLDER1="$1"
FOLDER2="$2"
OUTPUT_FILE="$3"

# Check if folders exist
if [ ! -d "$FOLDER1" ]; then
    echo "ERROR: Folder1 does not exist: $FOLDER1"
    exit 1
fi

if [ ! -d "$FOLDER2" ]; then
    echo "ERROR: Folder2 does not exist: $FOLDER2"
    exit 1
fi

echo "========================================"
echo "Comparing Folders"
echo "========================================"
echo "Folder 1: $FOLDER1"
echo "Folder 2: $FOLDER2"
echo "========================================"
echo ""

# Initialize counters
DIFF_COUNT=0
SAME_COUNT=0
MISSING_IN_FOLDER2=0
MISSING_IN_FOLDER1=0

# If output file specified, initialize it
if [ -n "$OUTPUT_FILE" ]; then
    echo "Results will be saved to: $OUTPUT_FILE"
    {
        echo "Folder Comparison Report"
        echo "================================"
        echo "Folder 1: $FOLDER1"
        echo "Folder 2: $FOLDER2"
        echo "Date: $(date)"
        echo "================================"
        echo ""
    } > "$OUTPUT_FILE"
fi

# Function to compare files
compare_files() {
    local file1="$1"
    local file2="$2"
    local relpath="$3"
    
    if [ -f "$file2" ]; then
        # Both files exist, compare them
        if git diff --no-index --quiet "$file1" "$file2" 2>/dev/null; then
            # Files are identical
            ((SAME_COUNT++))
            echo -e "${GREEN}[IDENTICAL]${NC} $relpath"
        else
            # Files are different
            ((DIFF_COUNT++))
            echo -e "${YELLOW}[DIFFERENT]${NC} $relpath"
            
            if [ -n "$OUTPUT_FILE" ]; then
                {
                    echo ""
                    echo "========================================"
                    echo "[DIFFERENT] $relpath"
                    echo "========================================"
                    git diff --no-index "$file1" "$file2" 2>&1
                } >> "$OUTPUT_FILE"
            else
                echo ""
                git diff --no-index --color "$file1" "$file2"
                echo ""
            fi
        fi
    else
        # File exists in folder1 but not in folder2
        ((MISSING_IN_FOLDER2++))
        echo -e "${RED}[MISSING IN FOLDER2]${NC} $relpath"
        
        if [ -n "$OUTPUT_FILE" ]; then
            echo "[MISSING IN FOLDER2] $relpath" >> "$OUTPUT_FILE"
        fi
    fi
}

# Compare files in folder1 with folder2
echo "Checking files in Folder 1..."
while IFS= read -r -d '' file1; do
    # Get relative path
    relpath="${file1#$FOLDER1/}"
    file2="$FOLDER2/$relpath"
    
    compare_files "$file1" "$file2" "$relpath"
done < <(find "$FOLDER1" -type f -print0)

# Check for files that exist in folder2 but not in folder1
echo ""
echo "Checking for files only in Folder 2..."
while IFS= read -r -d '' file2; do
    relpath="${file2#$FOLDER2/}"
    file1="$FOLDER1/$relpath"
    
    if [ ! -f "$file1" ]; then
        ((MISSING_IN_FOLDER1++))
        echo -e "${RED}[MISSING IN FOLDER1]${NC} $relpath"
        
        if [ -n "$OUTPUT_FILE" ]; then
            echo "[MISSING IN FOLDER1] $relpath" >> "$OUTPUT_FILE"
        fi
    fi
done < <(find "$FOLDER2" -type f -print0)

# Print summary
echo ""
echo "========================================"
echo "Summary"
echo "========================================"
echo "Identical files:     $SAME_COUNT"
echo "Different files:     $DIFF_COUNT"
echo "Missing in Folder 2: $MISSING_IN_FOLDER2"
echo "Missing in Folder 1: $MISSING_IN_FOLDER1"
echo "========================================"

# Save summary to output file if specified
if [ -n "$OUTPUT_FILE" ]; then
    {
        echo ""
        echo "========================================"
        echo "Summary"
        echo "========================================"
        echo "Identical files:     $SAME_COUNT"
        echo "Different files:     $DIFF_COUNT"
        echo "Missing in Folder 2: $MISSING_IN_FOLDER2"
        echo "Missing in Folder 1: $MISSING_IN_FOLDER1"
        echo "========================================"
    } >> "$OUTPUT_FILE"
    echo ""
    echo "Report saved to: $OUTPUT_FILE"
fi