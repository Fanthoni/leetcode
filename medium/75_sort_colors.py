from typing import List


class Solution:
    # Success
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []
        nums_0 = 0
        nums_1 = 0
        nums_2 = 0
        for i in range(len(nums)):
            if (nums[i] == 0):
                nums_0 += 1
            elif nums[i] == 1:
                nums_1 += 1
            else:
                nums_2 += 1

        nums.clear()
        nums.extend([0 for i in range(nums_0)])
        nums.extend([1 for i in range(nums_1)])
        nums.extend([2 for i in range(nums_2)])


Solution().sortColors([0, 1, 2])
