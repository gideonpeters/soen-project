from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    rolling_max_list = []
    max_num = float('-inf')
    for num in numbers:
        max_num = max(max_num, num)
        rolling_max_list.append(max_num)
    return rolling_max_list

print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]