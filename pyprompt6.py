from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    max_depth = 0
    curr_depth = 0
    
    for char in paren_string:
        if char == '(':
            curr_depth += 1
            if curr_depth > max_depth:
                max_depth = curr_depth
        elif char == ')':
            curr_depth -= 1
    
    result.append(max_depth)
    
    return result

print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]