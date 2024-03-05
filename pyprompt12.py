from typing import List, Optional 

def longest(strings: List[str]) -> Optional[str]: 
    if not strings:
        return None
    max_length = max(len(s) for s in strings)
    longest_str = [s for s in strings if len(s) == max_length][0]
    return longest_str

print(longest([]))
print(longest(['a', 'b', 'c']))
print(longest(['a', 'bb', 'ccc']))