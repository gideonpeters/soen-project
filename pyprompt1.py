from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    stack = []

    for char in paren_string:
        if char == '(':
            stack.append('')
        elif char == ')':
            if stack:
                result.append(''.join(stack))
                stack = []
    
    return result

print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']