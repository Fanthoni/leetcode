from copy import deepcopy
from typing import List


class Solution:
    # Success
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr = [i for i in range(1, k + 1)]
        end = list(reversed([n - i for i in range(k)]))

        res = []

        while curr != end:
            res.append(deepcopy(curr))
            curr = self.increaseByOne(curr, n)

        res.append(end)
        return res

    def increaseByOne(self, item: List[int], maxNum: int) -> List[int]:

        currIndex = -1

        while item[currIndex] == maxNum + currIndex + 1:
            currIndex -= 1
        item[currIndex] += 1

        for i in range(currIndex + 1, 0, 1):
            item[i] = item[i-1] + 1

        return item


# print(Solution().combine(4, 2))
# print(Solution().increaseByOne([2, 4, 5], 5))
