from typing import List
from math import pow


class Solution:
    # Success
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = map(lambda num: int(pow(num, 2)), nums)
        return sorted(squared)


sol = Solution()
print(sol.sortedSquares([-7, -3, 2, 3, 11]))
