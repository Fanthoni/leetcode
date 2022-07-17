from typing import List


class Solution:
    # Success
    def moveZeroes(self, nums: List[int]) -> None:
        zeroCounter = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCounter += 1

        for i in range(zeroCounter):
            nums.remove(0)
            nums.append(0)


sol = Solution()
sol.moveZeroes([0, 1, 0])
