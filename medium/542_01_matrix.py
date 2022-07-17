from typing import List


class Solution:
    # Success
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        res = mat

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                res[row][col] = float("+inf") if res[row][col] != 0 else 0

        for x in range(0, len(mat)):
            for y in range(0, len(mat[0])):

                if mat[x][y] != 0:
                    if x > 0:
                        mat[x][y] = min(mat[x][y], mat[x-1][y] + 1)
                    if y > 0:
                        mat[x][y] = min(mat[x][y], mat[x][y-1] + 1)

        for x in range(len(mat) - 1, -1, -1):
            for y in range(len(mat[0]) - 1, -1, -1):

                if mat[x][y] != 0:
                    if x < len(mat) - 1:
                        mat[x][y] = min(mat[x][y], mat[x+1][y] + 1)
                    if y < len(mat[0]) - 1:
                        mat[x][y] = min(mat[x][y], mat[x][y+1] + 1)

        return mat


Solution().updateMatrix([[0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [
    0, 0, 0, 1, 0], [1, 0, 1, 1, 1], [1, 0, 0, 0, 1]])
