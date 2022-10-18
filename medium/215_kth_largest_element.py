from heapq import heappop, heappush, heapify
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapify(heap)

        for num in nums:
            heappush(heap, num)
        sorted = [heappop(heap) for i in range(len(heap))]
        return sorted[len(sorted) - K]


input, K = [3, 2, 1, 1], 4
print(Solution().findKthLargest(input, K))
