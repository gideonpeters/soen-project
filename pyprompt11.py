from typing import List
def string_xor(a: str, b: str) -> str:
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result

print(string_xor('010', '110'))  # Output: '100'
