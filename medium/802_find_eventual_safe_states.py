from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        terminalNodes = [i for i, node in enumerate(graph) if len(node) == 0]
        res = []

        for i, node in enumerate(graph):
            if i not in terminalNodes:
                if False not in [True if neighbour in terminalNodes else False for neighbour in node]:
                    res.append(i)
        return sorted(res + terminalNodes)


print(Solution().eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
