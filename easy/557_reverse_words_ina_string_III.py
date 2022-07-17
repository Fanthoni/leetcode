class Solution:
    # Succcess
    def reverseWords(self, s: str) -> str:
        result = ""
        currIndex = 0

        while currIndex < len(s):
            if (s[currIndex] == " "):
                result += " "
                currIndex += 1
            else:
                indicesUntilNextSpace = self.findIndicesUntilNextSpace(
                    s, currIndex)
                currWord = s[currIndex:currIndex +
                             indicesUntilNextSpace:][::-1]
                result += currWord
                currIndex += indicesUntilNextSpace
        return result

    def findIndicesUntilNextSpace(slef, s: str, i: int) -> int:
        indicesUntilNextSpace = 0
        while i < len(s) and s[i] != " ":
            indicesUntilNextSpace += 1
            i += 1
        return indicesUntilNextSpace


sol = Solution()
print(sol.findIndicesUntilNextSpace("Let's take LeetCode contest", 6))
