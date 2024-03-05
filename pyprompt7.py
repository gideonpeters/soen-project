from typing import List 

def filter_by_substring(strings: List[str], substring: str) -> List[str]: 
    """
    Filter an input list of strings only for ones that contain given substring 
    """
    return [s for s in strings if substring in s]

# Test cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']