class Solution:
    # Success
    def longestPalindrome(self, s: str) -> int:

        if (len(s) <= 1):
            return len(s)

        s = sorted()

        soloCharExists = False
        counter = 0
        prevChar = ""
        palindromeCount = 0

        while counter < len(s):
            if (prevChar != "" or counter == 0) and (counter + 1 >= len(s) or s[counter + 1] != s[counter]):
                soloCharExists = True
                prevChar = s[counter]
                counter += 1
            elif s[counter + 1] == s[counter]:
                palindromeCount += 2
                prevChar = s[counter]
                counter += 2
            else:
                prevChar = s[counter]
                counter += 1

        return palindromeCount + 1 if soloCharExists else palindromeCount


print(Solution().longestPalindrome("ccc"))
