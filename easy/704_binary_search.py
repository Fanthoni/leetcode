from typing import List
from math import floor


class Solution:
    # Time limit exceeded
    def search(self, nums: List[int], target: int) -> int:
        leftPoint = 0
        rightPoint = len(nums)
        midPoint = floor(len(nums) / 2)

        while (rightPoint > leftPoint):
            if nums[midPoint] == target:
                return midPoint
            if nums[midPoint] > target:
                # search left side
                rightPoint = midPoint
            elif nums[midPoint] < target:
                # search right
                leftPoint = midPoint
            midPoint = floor((rightPoint + leftPoint) / 2)
        return -1


sol = Solution()
print(sol.search([-1, 0, 3, 5, 9, 12], 5))
