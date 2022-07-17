from typing import List


class Solution:
    # Succss
    def partitionLabels(self, s: str) -> List[int]:
        if len(s) <= 1:
            return [len(s)]

        intervals = {}

        for i, char in enumerate(s):
            if char not in intervals:
                intervals[char] = [i, i]
            else:
                intervals[char][1] = i

        intervals = intervals.values().sort()
        res = []

        currMin = interval[0][0]
        currMax = interval[0][1]

        for i, interval in enumerate(intervals):
            if interval[0] > currMax:
                res.append(currMax - currMin + 1)
                currMin, currMax = interval[0], interval[1]
            elif interval[0] < currMax and interval[1] > currMax:
                currMax = interval[1]

        return res


testData = "ababcbacadefegdehijhklij"

Solution().partitionLabels(testData)
