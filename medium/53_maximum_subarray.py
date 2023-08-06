from typing import List


class Solution:

    # Dynamic Programming
    def maxSubArray(self, nums: List[int]) -> int:

        dp = [0]*len(nums)
        dp[0] = nums[0]
        curr_max = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            if dp[i] > curr_max:
                curr_max = dp[i]
        return curr_max
