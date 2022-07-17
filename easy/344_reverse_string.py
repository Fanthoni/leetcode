from typing import List


class Solution:
    # Success
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        N = len(s) // 2
        for i in range(N):
            # p1, p2 = s[i], s[len(s) - i - 1]
            temp = s[i]
            s[i] = s[len(s) - i - 1]
            s[len(s) - 1 - i] = temp
        # return s


sol = Solution()
print(sol.reverseString(["h", "e", "l", "l", "o", "h"]))
