from typing import List 
def intersperse(numbers: List[int], delimiter: int) -> List[int]: 
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i != len(numbers) - 1: 
            result.append(delimiter)
    return result

print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3] 