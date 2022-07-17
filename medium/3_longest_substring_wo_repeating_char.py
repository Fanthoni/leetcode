class Solution:
    # Success
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        longestSubStrLen = 0
        currSubStr = ""

        for char in s:
            if currSubStr.find(char) != -1:
                currSubStr = currSubStr[currSubStr.find(char) + 1::]
            currSubStr += char
            longestSubStrLen = max(longestSubStrLen, len(currSubStr))
        return longestSubStrLen

        # while currIndex < len(s):
        #     if currSubStr.index(s[currIndex]) == -1:
        #         currSubStr += s[currIndex]
        #         currIndex += 1
        #     else:
        #         currSubStr
