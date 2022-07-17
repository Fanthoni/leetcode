class Solution:
    # Success
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        carryOver = 0

        while num1 != "" or num2 != "" or carryOver != 0:
            num1Value = ord(num1[-1]) - 48 if num1 != "" else 0
            num2Value = ord(num2[-1]) - 48 if num2 != "" else 0

            currSum = (num1Value + num2Value) + carryOver

            res = str(currSum % 10) + res
            carryOver = currSum // 10

            num1 = num1[:-1:]
            num2 = num2[:-1:]

        return res


print(Solution().addStrings("999", "99"))
