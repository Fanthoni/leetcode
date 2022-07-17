from copy import deepcopy
from typing import List


class Solution:
    # Time limit exceeded
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        for i in range(len(nums) - 2):
            complement = nums[i] * -1

            searchNums = nums[i+1::]
            allComplementIndices = self.twoSum(searchNums, complement)

            for arrOfInd in allComplementIndices:
                currTriplet = sorted([nums[i], searchNums[arrOfInd[0]],
                                      searchNums[arrOfInd[1]]])
                answer.append(
                    currTriplet) if currTriplet not in answer else None
        return answer

    '''
    Returns array of arrays containing the indices of the numbers that sums up to the target value
    '''

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if (len(numbers) < 2):
            return []

        complements = []
        answer = []
        numbers = deepcopy(numbers)
        for i in range(len(numbers)):
            if numbers[i] in complements:
                answer.append([numbers.index(target - numbers[i]), i])

                complements.remove(numbers[i])
                numbers[numbers.index(target - numbers[i])] = "False"
                numbers[i] = "False"
            else:
                complements.append(target - numbers[i])
        return answer

    # Can use binary search using two pointers starting from i + 1 and len(nums)
    # to search for the target combination
    # https://leetcode.com/problems/3sum/discuss/7498/Python-solution-with-detailed-explanation#:~:text=1%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20continue-,Code,-class%20Solution(


sol = Solution()
testArr = [-1, -2, -3, 4, 1, 3, 0, 3, -2, 1, -2, 2, -1, 1, -5, 4, -3]
testArr2 = [-3, 4, 1, 3, 0, 3, -2, 1, -2, 2, -1, 1, -5, 4, -3]
# print(sol.threeSum(testArr))
print(sol.twoSum(testArr2, 2))
