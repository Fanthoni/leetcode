from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newNums = []

        for i, num in enumerate(nums):
            # if current number is diff from prev num OR index = 0
                # add the current number to the newNums
            # if curr number is the same as prev num AND the currentIndex and the first index is less than 2
                # add the current number to the newNums

            if i == 0 or num != nums[i - 1]:
                newNums.append(num)
            elif num == nums[i-1] and i - nums.index(num) < 2:
                newNums.append(num)

        for i, num in enumerate(newNums):
            nums[i] = newNums[i]
            
        return len(newNums)

        
    
sol = Solution()
input = [1, 1, 2, 2, 2, 2, 3]
print(sol.removeDuplicates(input))
print(input)

        