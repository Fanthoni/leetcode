from operator import add
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        addedInterval = []

        for interval in intervals:
            if len(addedInterval) == 0:
                addedInterval.append(interval)
            else:
                prevInterval = addedInterval[-1]
                if interval[0] not in range(prevInterval[0], prevInterval[1]):

        return len(intervals) - len(addedInterval)


testData = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(Solution().eraseOverlapIntervals)
