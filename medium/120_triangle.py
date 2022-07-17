from typing import List


class Solution:
    # Success
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        prevLevelSum = triangle[0]
        for i in range(1, len(triangle)):
            currLevelSum = triangle[i]
            for j, num in enumerate(currLevelSum):
                if j == 0:
                    currLevelSum[j] += prevLevelSum[0]
                elif j == len(currLevelSum) - 1:
                    currLevelSum[j] += prevLevelSum[j-1]
                else:
                    currLevelSum[j] = min(
                        currLevelSum[j] + prevLevelSum[j - 1], currLevelSum[j] + prevLevelSum[j])

            prevLevelSum = currLevelSum

        return min(prevLevelSum)


print(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
