from typing import List


class Solution:
    # Success
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            rightSum -= nums[i]

            leftSum += nums[i-1] if i > 0 else 0

            if rightSum == leftSum:
                return i
        return -1


sol = Solution()
testData = [1, 7, 3, 6, 5, 6]
print(sol.pivotIndex(testData))
