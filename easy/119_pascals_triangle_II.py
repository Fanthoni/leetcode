from turtle import left
from typing import List


class Solution:
    # Success
    def getRow(self, rowIndex: int) -> List[int]:
        rowValues = [[1]]
        for i in range(1, rowIndex + 1):
            currRowValues = []
            prevRowValues = rowValues[-1]

            for j in range(i + 1):
                leftVal = prevRowValues[j-1] if j - 1 >= 0 else 0
                rightVal = prevRowValues[j] if j < len(prevRowValues) else 0
                currRowValues.append(leftVal + rightVal)

            rowValues.append(currRowValues)

        return rowValues[-1]
