from typing import List


class Solution:
    # Success
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == k:
            return
        if k > len(nums):
            k = k % len(nums)

        temp = (nums[-k::] + nums[:-k:])
        nums.clear()
        nums.extend(temp)


sol = Solution()
nums = [1, 2, 3, 4]
sol.rotate(nums, 5)
print(nums)
