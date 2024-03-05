from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    deviations = [abs(x - mean) for x in numbers]
    return sum(deviations) / len(deviations)

print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0