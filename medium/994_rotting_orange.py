from copy import deepcopy
from typing import List

# Failed
# https://zhenyu0519.github.io/2020/03/25/lc994/#related-topic
# def orangesRotting(self, grid: List[List[int]]) -> int:

#     currLongestRottTime = 0

#     for row in range(len(grid)):
#         for col in range(len(grid[0])):
#             if grid[row][col] == 1 and self.isFreshOrangeTrapped(grid, row, col):
#                 return -1

#             if grid[row][col] == 2:
#                 currLongestRottTime = max(
#                     currLongestRottTime, self.getLongestTimeToRot(deepcopy(grid), col, row))

#     return currLongestRottTime

# def getLongestTimeToRot(self, grid, col, row) -> int:
#     grid[row][col] = 2

#     currMax = 0
#     if row > 0 and grid[row-1][col] == 1:
#         currMax = max(self.getLongestTimeToRot(
#             grid, col, row-1) + 1, currMax)
#     if col > 0 and grid[row][col-1] == 1:
#         currMax = max(self.getLongestTimeToRot(
#             grid, col-1, row) + 1, currMax)

#     if row < len(grid) - 1 and grid[row+1][col] == 1:
#         currMax = max(self.getLongestTimeToRot(
#             grid, col, row+1) + 1, currMax)
#     if col < len(grid[0]) - 1 and grid[row][col+1] == 1:
#         currMax = max(self.getLongestTimeToRot(
#             grid, col+1, row) + 1, currMax)

#     return currMax

# def isFreshOrangeTrapped(self, grid, row, col):
#     left = grid[row][col-1] if col > 0 else 0
#     top = grid[row-1][col] if row > 0 else 0
#     right = grid[row][col+1] if col < len(grid[0]) - 1 else 0
#     bot = grid[row+1][col] if row < len(grid) - 1 else 0

#     return left == 0 and top == 0 and right == 0 and bot == 0


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        fresh = []
        direction = {
            "LEFT": [0, -1],
            "RIGHT": [0, 1],
            "UP": [-1, 0],
            "DOWN": [1, 0]
        }
        minCount = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    rotten.append([row, col])
                elif grid[row][col] == 1:
                    fresh.append([row, col])

        while len(rotten) > 0:
            # newRotAdded = False
            nextRotQ = []
            for i in range(len(rotten)):
                rottenOrange = rotten.pop()
                row, col = rottenOrange[0], rottenOrange[1]
                if row > 0:
                    topItem = self.addTwoArr(rottenOrange, direction["UP"])
                    if topItem in fresh:
                        fresh.remove(topItem)
                        nextRotQ.append(topItem)
                        # newRotAdded = True
                if col > 0:
                    leftItem = self.addTwoArr(rottenOrange, direction["LEFT"])
                    if leftItem in fresh:
                        fresh.remove(leftItem)
                        nextRotQ.append(leftItem)
                        # newRotAdded = True

                if row < len(grid) - 1:
                    bottomItem = self.addTwoArr(
                        rottenOrange, direction["DOWN"])
                    if bottomItem in fresh:
                        fresh.remove(bottomItem)
                        nextRotQ.append(bottomItem)
                        # newRotAdded = True

                if col < len(grid[0]) - 1:
                    rightItem = self.addTwoArr(
                        rottenOrange, direction["RIGHT"])
                    if rightItem in fresh:
                        fresh.remove(rightItem)
                        nextRotQ.append(rightItem)
                        # newRotAdded = True

            minCount += 1 if len(nextRotQ) > 0 else 0
            rotten.extend(nextRotQ)

        if len(fresh) > 0:
            return -1
        else:
            return minCount

    def addTwoArr(self, arr1, arr2):
        return [arr1[0] + arr2[0], arr1[1] + arr2[1]]


Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
