from typing import List


class Solution:
    # Success
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 0:
            return 0
        elif N == 1:
            return nums[0]
        elif N == 2:
            return max(nums[0], nums[1])
        else:
            currIndex = 3
            nums = [0] + nums
            while currIndex < len(nums):
                nums[currIndex] = max(
                    nums[currIndex - 3] + nums[currIndex], nums[currIndex - 2] + nums[currIndex])
                currIndex += 1
            return max(nums[-1], nums[-2])


print(Solution().rob([2, 1, 1, 2]))
