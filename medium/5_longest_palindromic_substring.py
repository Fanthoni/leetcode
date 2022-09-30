class Solution:
    # Success
    def longestPalindrome(self, s: str) -> str:
        N = len(s)

        if N <= 1:
            return s

        longestSubStr = s[0]
        for i in range(len(s)):
            currPalindrome = s[i]
            start = end = i

            while end < N - 1 and s[end+1] == s[i]:
                currPalindrome += s[i]
                end += 1

            while start > 0 and end < N-1 and self.isPalindrome(f"{s[start-1]}{currPalindrome}{s[end+1]}"):
                currPalindrome = f"{s[start-1]}{currPalindrome}{s[end+1]}"
                start, end = start-1, end+1

            if len(currPalindrome) > len(longestSubStr):
                longestSubStr = currPalindrome

        return longestSubStr

    def isPalindrome(self, s: str) -> bool:
        front, back = 0, len(s) - 1

        while back > front:
            if s[front] != s[back]:
                return False
            front, back = front + 1, back - 1
        return True


print(Solution().longestPalindrome("babac"))
