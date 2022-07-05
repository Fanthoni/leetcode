from typing import List


class Solution:
    # Success
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i != 0:
                nums[i] += nums[i-1]
        return nums


sol = Solution()
testData = [1, 2, 3, 4, 5]
print(sol.runningSum(testData))
