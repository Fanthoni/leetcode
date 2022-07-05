# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # Success
    def firstBadVersion(self, n: int) -> int:
        # initiate left and right to 0 and len - 1
        # initiate midpoint

        # if curent is bad
        # if prev version is good return this index
        # else move the right point to the midpoint
        # elif current is god
        # if next is bad return next index
        # else move the left  to the current midpoint
        # establish the new endpopint

        if isBadVersion(0):
            return 0
        elif not isBadVersion(n):
            return n

        left, right = 0, n
        midpoint = n // 2

        while True:
            if isBadVersion(midpoint):
                if not isBadVersion(midpoint - 1):
                    return midpoint
                else:
                    right = midpoint - 1
            else:
                if isBadVersion(midpoint + 1):
                    return midpoint + 1
                else:
                    left = midpoint + 1
            midpoint = (left + right) // 2


sol = Solution()
sol.firstBadVersion(5)
