import math


class Solution:
    # incomplete
    def divide(self, dividend: int, divisor: int) -> int:
        isResultNegative = ((dividend < 0 or divisor < 0)
                            and (dividend > 0 or divisor > 0))
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0

        if (divisor == 1):
            count = dividend
        else:
            while (dividend >= divisor):
                dividend -= divisor
                count += 1

        if (isResultNegative):
            count = count * -1

        if (count > math.pow(2, 31) - 1):
            return int(math.pow(2, 31)) - 1
        elif (count < math.pow(2, 31) * -1):
            return int(math.pow(2, 31) * -1)
        else:
            return count


sol = Solution()
print(sol.divide(-2147483648, -1))
