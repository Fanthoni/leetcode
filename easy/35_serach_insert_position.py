from typing import List


class Solution:

    # Success
    def searchInsert(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1
        midpoint = (right + left) // 2

        while right > left:
            if nums[midpoint] == target:
                return midpoint

            if target < nums[midpoint]:
                # shift right to the left
                right = midpoint - 1 if midpoint > 0 else 0
            elif target > nums[midpoint]:
                # shift left to the right
                left = midpoint + 1
            midpoint = (right + left) // 2

        if nums[midpoint] == target:
            return midpoint

        if nums[midpoint] > target:
            return midpoint
        else:
            return midpoint + 1


sol = Solution()
testData = [1, 3]
print(sol.searchInsert(testData, 0))
