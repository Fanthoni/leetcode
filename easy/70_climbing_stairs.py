class Solution:
    # Success
    def climbStairs(self, n: int) -> int:
        prevRes = [0, 1, 2]

        if n in prevRes:
            return prevRes[n]
        else:
            while len(prevRes) < n + 1:
                prevRes.append(prevRes[-1] + prevRes[-2])
            return prevRes[-1]


print(Solution().climbStairs(2))
