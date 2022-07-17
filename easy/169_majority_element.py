from typing import List


class Solution:
    # Success
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        majoritySize = len(nums) // 2
        nums = sorted(nums)

        currNum = None
        currNumCount = 0

        for num in nums:
            if currNum != num:
                currNum = num
                currNumCount = 1
            else:
                currNumCount += 1
                if currNumCount > majoritySize:
                    return currNum
