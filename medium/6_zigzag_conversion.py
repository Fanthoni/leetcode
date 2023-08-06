from typing import List

"""
UNSOLVED
"""
class Solution:
    def parition(self, s: str, numRows: int) -> List[str]:
        parition = list()
        isReversed = False
        
        currPartition = ""
        for char in s:
            currPartition += char

            if (not isReversed and len(currPartition) == numRows) or (isReversed and len(currPartition) == numRows - 2):
                parition.append(currPartition)
                currPartition = ""
                if numRows > 2:
                    isReversed = not isReversed

        return parition

    def convert(self, s: str, numRows: int) -> str:
        """
        separate the string into partition array of array with alternating numrows and numrows - 2 in length

        instantiate a variable to flip back and forth between revers and not reversed
        for each sentence in the array categorize them from 0 to numrows - 1

        if isReversed,
        categorize starting numrows - 2 to 1
        """
        if numRows == 1:
            return s





sol = Solution()
sol.convert("PAYPALISHIRING", 3)