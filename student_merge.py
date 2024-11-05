from collections import defaultdict, Counter

def merge_with_defaultdict(*dicts):
    """
    Merges multiple word frequency dictionaries into a single dictionary, 
    combining frequencies of identical words. Uses a defaultdict to accumulate 
    word counts from each dictionary.

    Args:
        *dicts: An arbitrary number of dictionaries to merge, where each key is a 
                word (str) and each value is its frequency (int).

    Returns:
        dict: A dictionary with all words from the input dictionaries and their 
              combined frequencies. The dictionary is sorted by frequency in 
              descending order if the bonus sorting feature is implemented.
    """    
    # Using defaultdict to accumulate word frequencies across all dictionaries
    merged = defaultdict(int)
    for d in dicts:
        for word, freq in d.items():
            merged[word] += freq
    
    # Optional: Sort by frequency in descending order for the bonus requirement
    sorted_merged = dict(sorted(merged.items(), key=lambda x: x[1], reverse=True))
    return sorted_merged

def merge_with_counter(*dicts):
    """
    Merges multiple word frequency dictionaries into a single dictionary, 
    combining frequencies of identical words. Uses a Counter to sum frequencies 
    from each dictionary directly.

    Args:
        *dicts: An arbitrary number of dictionaries to merge, where each key is a 
                word (str) and each value is its frequency (int).

    Returns:
        dict: A dictionary with all words from the input dictionaries and their 
              combined frequencies. The dictionary is sorted by frequency in 
              descending order if the bonus sorting feature is implemented.
    """    
    # Using Counter to sum frequencies directly
    merged = Counter()
    for d in dicts:
        merged.update(d)
    
    # Optional: Sort by frequency in descending order for the bonus requirement
    sorted_merged = dict(merged.most_common())
    return sorted_merged
