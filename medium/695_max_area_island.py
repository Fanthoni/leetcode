from typing import List, Optional


class Solution:
    # Succss
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        currMaxCoverage = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if (grid[row][col] == 1):
                    islandCoverage = self.explore(grid, row, col)
                    currMaxCoverage = max(currMaxCoverage, islandCoverage)

        return currMaxCoverage

    def explore(self, grid, row, col) -> int:

        if grid[row][col] != 1:
            return 0

        R, C = len(grid), len(grid[0])
        totalVisited = 1
        grid[row][col] = "V"

        if row + 1 < R:
            totalVisited += self.explore(grid, row + 1, col)
        if row - 1 >= 0:
            totalVisited += self.explore(grid, row - 1, col)
        if col + 1 < C:
            totalVisited += self.explore(grid, row, col + 1)
        if col - 1 >= 0:
            totalVisited += self.explore(grid, row, col - 1)

        return totalVisited
