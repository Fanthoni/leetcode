from typing import List


class Solution:
    # Success
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        for i in range(len(s)):
            if s[i] not in mapping.keys():
                if t[i] not in mapping.values():
                    mapping[s[i]] = t[i]
                else:
                    return False
            elif t[i] != mapping[s[i]]:
                return False
        return True
        # return self.indicize(s) == self.indicize(t)

    # def indicize(self, s: str) -> List[str]:
    #     registeredChar = []
    #     sequencePattern = []
    #     for c in s:
    #         if c not in registeredChar:
    #             registeredChar.append(c)
    #         sequencePattern.append(registeredChar.index(c))
    #     return sequencePattern


sol = Solution()
print(sol.isIsomorphic("egh", "add"))
