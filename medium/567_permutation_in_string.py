class Solution:
    # Success
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) == 0 or s1 == s2:
            return True

        originalS1 = s1
        currSubStr = ""

        for char in s2:
            if s1.find(char) != -1:
                currSubStr += char
                s1 = s1.replace(char, "", 1)
            elif originalS1.find(char) == -1:
                currSubStr = ""
                s1 = originalS1
            else:
                indexOfCharInSubStr = currSubStr.find(char)
                preCurrSubStr = currSubStr[0:indexOfCharInSubStr + 1]
                currSubStr = currSubStr[indexOfCharInSubStr + 1::]
                currSubStr += char
                s1 += preCurrSubStr
                s1 = s1.replace(char, "", 1)

            if len(s1) == 0:
                return True

        return False


Solution().checkInclusion("adc", "dcda")
