from typing import List


class Solution:
    # Failed:
    #  https://medium.com/@xiaogegexiao/increasing-triplet-subsequence-problem-995471b338f1
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return False

        numsWithIndex = []
        for i in range(len(nums)):
            numsWithIndex.append([nums[i], i])

        numsWithIndex.sort()

        for i in range(len(nums) - 2):
            if numsWithIndex[i][1] < numsWithIndex[i+1][1] and numsWithIndex[i+1][1] < numsWithIndex[i+2][1]:
                return True
        return False


Solution().increasingTriplet([2, 1, 5, 0, 4, 6])
