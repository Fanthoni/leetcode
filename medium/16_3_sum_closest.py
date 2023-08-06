from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        best = nums[0] + nums[1] + nums[len(nums) - 1]
        nums = sorted(nums)

        for index in range(len(nums) - 2):
            start = index + 1
            end = len(nums) - 1

            while start < end:
                currSum = nums[index] + nums[start] + nums[end]
                if currSum > target: end -= 1
                else: start += 1
                
                if abs(target - currSum) < abs(target - best): best = currSum
                if target - currSum == 0: break
        return best
            

sol = Solution()
sol.threeSumClosest([0, 1, 0, -1], 1)