from copy import deepcopy
from typing import List


class Solution:
    # Success
    def rotate(self, matrix: List[List[int]]) -> None:
        arrayCopy, N = deepcopy(matrix), len(matrix)
        for i in range(N):
            currRow = arrayCopy[i]

            for j in range(N):
                matrix[j][N - 1 - i] = currRow[j]
