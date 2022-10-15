class Solution:
    # Dynamic Programming
    def numSquares(self, n: int) -> int:
        # keep track of the next square
        # for each dp
        # if dp == square set the val to 1
        # else start from front and back sequentially and find the minimum total sum
        # set the minimum to the current dp
        # return dp[i]

        dp = [float("inf")] * (n + 1)
        nextPerfectSquareBase = 1

        for i in range(1, len(dp)):
            if (i == pow(nextPerfectSquareBase, 2)):
                dp[i] = 1
                nextPerfectSquareBase += 1
            else:
                startP, endP = 1, i - 1
                while (startP <= endP):
                    dp[i] = min(dp[i], (dp[startP] + dp[endP]))
                    startP += 1
                    endP -= 1
        print(dp)
        return dp[n]

    # # BFS - Time Limit Exceeded
    # def numSquares(self, n: int) -> int:
    #     # for every number until next square is bigger than 1, build a list of perfect squares
    #     # for every square in the list of perfect squares
    #     # reduce the goal by that number
    #     # append the results in an array

    #     nextPerfectSquareBase = 1
    #     perfectSquares = []
    #     while (pow(nextPerfectSquareBase, 2) <= n):
    #         perfectSquares.append(pow(nextPerfectSquareBase, 2))
    #         nextPerfectSquareBase += 1

    #     Q = []
    #     currLevelResult = [n]
    #     while (0 not in currLevelResult):
    #         Q.append(currLevelResult)
    #         prevLevelResult = currLevelResult

    #         currLevelResult = []
    #         for preVal in prevLevelResult:
    #             for square in perfectSquares:
    #                 if (preVal - square >= 0):
    #                     currLevelResult.append(preVal - square)
    #                 else:
    #                     break
    #     return len(Q)


print(Solution().numSquares(7168))
