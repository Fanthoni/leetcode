from itertools import count
import math


class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0

        nth_bit = 0
        while math.pow(2, nth_bit) <= n:
            nth_bit += 1

        count_1 = 0
        while n > 1:
            if math.pow(2, nth_bit) <= n:
                count_1 += 1
                n -= math.pow(2, nth_bit)
            nth_bit -= 1

        return count_1 + 1 if n == 1 else count_1


print(Solution().hammingWeight())
