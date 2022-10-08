from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 1. top move  -> append the first array
        # 2. right move -> append the last element in every array from 0th to Nth
        # 3. bottom move -> append the revers of the last array
        # 4. left move -> append the first element in every array from Nth to 0th

        strategy = 1
        res = []
        while len(matrix) > 0:
            if strategy == 1:
                res += (matrix.pop(0))
            elif strategy == 2:
                res += ([x.pop(-1) for x in matrix])
            elif strategy == 3:
                res += list(reversed(matrix.pop(-1)))
            else:
                res += list(reversed([x.pop(0) for x in matrix]))

            matrix = list(filter(lambda x: len(x) > 0, matrix))

            # Set next strategy
            if strategy <= 3:
                strategy += 1
            else:
                strategy = 1

        return res


print(Solution().spiralOrder([[7], [9], [6]]))
