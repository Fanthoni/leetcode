from typing import List


class Solution:
    # Success
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [([0 for i in range(n)]) for i in range(n)]

        currLayer, N = 0, n - 1
        currNum = 1
        toAddThisLayer = N

        for i in range(n // 2):
            for j in range(toAddThisLayer):
                res[currLayer][currLayer + j] = currNum
                res[currLayer + j][N - currLayer] = currNum + \
                    (1 * toAddThisLayer)
                res[N - currLayer][N - currLayer -
                                   j] = currNum + (2 * toAddThisLayer)
                res[N - currLayer - j][currLayer] = currNum + \
                    (3 * toAddThisLayer)
                currNum += 1

            currNum += (toAddThisLayer * 3)
            currLayer += 1
            toAddThisLayer -= 2

        if currNum == n*n:
            res[currLayer][currLayer] = currNum
        return res


print(Solution().generateMatrix(5))
