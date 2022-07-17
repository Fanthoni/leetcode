from typing import List


class Solution:
    # Success
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        currIndex = 0

        def dfs(path):
            if len(path) == len(s):
                res.append(path)
            else:
                currChar = s[len(path)]
                if currChar.isdigit():
                    dfs(path + currChar)
                else:
                    dfs(path + currChar.upper())
                    dfs(path + currChar.lower())

        dfs("")
        return res


# print(Solution().letterCasePermutation(""))
