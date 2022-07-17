class Solution:
    # Success
    def multiply(self, num1: str, num2: str) -> str:
        currTrailingZero = 1
        res = 0

        for i in range(len(num1) - 1, -1, -1):

            currInnerDigit = 1
            currNum1 = ord(num1[i:i+1]) - 48
            carryOver = 0
            for j in range(len(num2) - 1, -1, -1):
                currNum2 = ord(num2[j:j+1]) - 48
                res += ((currNum1 * currNum2) % 10 + carryOver) * \
                    currInnerDigit * currTrailingZero

                currInnerDigit *= 10
                carryOver = (currNum1 * currNum2) // 10

            if carryOver != 0:
                res += carryOver * currInnerDigit * currTrailingZero

            currTrailingZero *= 10

        return str(res)


Solution().multiply("123", "456")
