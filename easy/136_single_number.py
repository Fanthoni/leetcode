from typing import List


class Solution:
    # Success
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i + 1] != nums[i]:
                return nums[i]
            else:
                nums.remove(nums[i])


sol = Solution()
sol.singleNumber([2, 2, 1, 1, 5])
