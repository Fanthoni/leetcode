from typing import List


class Solution:
    # # DFS - Time limit exceeded
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     if (len(s) == 0):
    #         return True

    #     prefixes = [word for word in wordDict if s.startswith(word)]
    #     if len(prefixes) == 0:
    #         return False

    #     res = []
    #     for prefix in prefixes:
    #         breakable = self.wordBreak(s[len(prefix):], wordDict)
    #         res.append(breakable)
    #     return True in res

    # Dynamic Programming
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s), -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i: i + len(word)] == word:
                    dp[i] = True and dp[i + len(word)]
                if (dp[i] == True):
                    break
                # if index i + length of the word is shorter than the length of the string and string[i:i + len(word)] == word
                # dp[i] = True and dp[i + len(word) + 1]
                # if dp[i] == True: break
        return dp[0]


input = "catsanddog"
dict = ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(input, dict))
