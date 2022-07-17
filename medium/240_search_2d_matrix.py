from typing import List


class Solution:
    # Success
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, y = len(matrix) - 1, 0

        while True:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                if y + 1 < len(matrix[0]):
                    y += 1
                else:
                    return False
            elif matrix[x][y] > target:
                if x - 1 >= 0:
                    x -= 1
                else:
                    return False
