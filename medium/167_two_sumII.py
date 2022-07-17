from typing import List


class Solution:
    # Success
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        complements = []
        for i in range(len(numbers)):
            if numbers[i] in complements:
                return [numbers.index(target - numbers[i]) + 1, i + 1]
            elif target - numbers[i] not in complements:
                complements.append(target - numbers[i])
