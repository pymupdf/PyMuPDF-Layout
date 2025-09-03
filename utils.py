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

