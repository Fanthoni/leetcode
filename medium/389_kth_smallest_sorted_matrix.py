from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxHeap = []
        for row in matrix:
            for item in row:
                maxHeap.append(item)
        maxHeap = list(reversed(sorted(maxHeap)))
        print(maxHeap)
        while len(maxHeap) > k:
            maxHeap.pop(0)
        return maxHeap[0]


print(Solution().kthSmallest([[1, 2], [3, 3]], 1))
