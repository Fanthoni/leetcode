class Solution:
    # Success
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        elif s == t:
            return True

        for i in range(len(s) - 1):
            if s[i] in t:
                t = self.removeSlice(s[i], t)
                print(t)
            else:
                return False
        return True

    def removeSlice(self, s: str, t: str) -> str:
        return t[t.index(s) + 1::]


sol = Solution()
print(sol.isSubsequence("ace", "abcde"))
