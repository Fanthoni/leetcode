from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # point one pointer at the beginning and at the end
        # two pointer is not on the same index
        # move the smaller pointer to the right/left
        # compute the current area and if it beats the best so far

        leftP, rightP = 0, len(height) - 1
        bestMaxArea = float("-inf")

        while (leftP != rightP):
            currArea = (rightP - leftP) * min(height[leftP], height[rightP])
            if currArea > bestMaxArea:
                bestMaxArea = currArea
            if height[rightP] < height[leftP]:
                rightP -= 1
            else:
                leftP += 1

        return bestMaxArea
