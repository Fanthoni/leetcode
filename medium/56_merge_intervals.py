from typing import List


class Solution:
    # Success
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        res = []
        interval.sort()
        for interval in intervals:
            if (len(res) == 0):
                res.append(interval)
            else:
                lastInterval = res[-1]
                if interval[0] <= lastInterval[1]:
                    if interval[0] < lastInterval[0]:
                        res[-1][0] = interval[0]
                    if interval[1] > lastInterval[1]:
                        res[-1][1] = interval[1]
                else:
                    res.append(interval)
        return res
