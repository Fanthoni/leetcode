

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n < 0):
            return False

        bin = format(n, "b")
        return not (bin.count("1") > 1 or bin.count("1") == 0)


Solution().isPowerOfTwo(-16)
