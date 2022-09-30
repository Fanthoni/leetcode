class Solution:
    # Failed
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        elif s1 + s2 == s3 or s2 + s1 == s3:
            return True
        else:
            s1Pointer = 0
            s2Pointer = 0

            toObserveNext = s1 if s3[0] == s1[0] else s2
            currIndex = 0

            while currIndex < len(s3):
                # if s1[s1Pointer] != s3[currIndex] and s2[s2Pointer] != s3[currIndex]:
                #     return False

                toIncrease = s1Pointer if toObserveNext == s1 else s2Pointer

                if toIncrease >= len(toObserveNext) or toObserveNext[toIncrease] != s3[currIndex]:
                    return False

                while toIncrease < len(toObserveNext) and toObserveNext[toIncrease] == s3[currIndex]:
                    toIncrease += 1
                    currIndex += 1

                if toObserveNext == s1:
                    toObserveNext = s2
                    s1Pointer = toIncrease
                else:
                    toObserveNext = s1
                    s2Pointer = toIncrease
                # toObserveNext = s1 if toObserveNext == s2 else s2

            return True


print(Solution().isInterleave("aa", "ab",  "aaba"))
