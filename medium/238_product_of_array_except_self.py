from typing import List


class Solution:

    # Success
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        containsZero = False
        containsMultipleZero = False
        totalProductWithoutZero = 1

        for i in range(0, len(nums)):
            if nums[i] == 0:
                containsMultipleZero = True if containsZero else False
                containsZero = True
            else:
                totalProductWithoutZero *= nums[i] if nums[i] != 0 else 1

        if containsMultipleZero:
            return [0 for i in range(len(nums))]

        res = []
        for num in nums:
            if containsZero:
                if num != 0:
                    res.append(0)
                else:
                    res.append(totalProductWithoutZero)
            else:
                res.append(totalProductWithoutZero // num)

        return res


print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))
