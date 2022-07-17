from math import factorial
from typing import List


class Solution:
    # Failed
    # https://blog.csdn.net/fuxuemingzhu/article/details/79363903#:~:text=28-,The%20Python%20code%20is%20as%20follows%3A,twenty%20one,-date

    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     if len(nums) <= 1:
    #         return [[]] if len(nums) == 0 else [[nums[0]]]

    #     res = []
    #     currFactor = 1
    #     N = len(nums)

    #     while currFactor < N:
    #         for i, num in enumerate(nums):
    #             currPerm = [num]
    #             for j in range(1, N, 1):
    #                 currPerm.append(nums[(i + currFactor*j) % N])
    #             res.append(currPerm)

    #         currFactor += 1

    #     return res

    def permute(self, nums):
        visited = [0] * len(nums)
        res = []

        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
            else:
                for i in range(len(nums)):
                    if not visited[i]:
                        visited[i] = 1
                        dfs(path + [nums[i]])
                        visited[i] = 0

        dfs([])
        return res

# print(Solution().permute([]))
