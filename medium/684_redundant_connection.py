from copy import deepcopy
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        reversedEdges = list(reversed(edges))

        for i, edge in enumerate(reversedEdges):
            curr_graph = deepcopy(reversedEdges)
            curr_graph.remove(edge)
            if (self.isTree(curr_graph, N)):
                return edge

    def isTree(self, edges: List[List[int]], N: int) -> bool:
        visitedStatus = [False] * (N + 1)
        Q = [edges[0][0]]

        while len(Q) > 0:
            currNode = Q.pop(0)
            if (visitedStatus[currNode] == True):
                return False
            else:
                visitedStatus[currNode] = True
                for u, v in deepcopy(edges):
                    if currNode in [u, v]:
                        if u != currNode:
                            Q.append(u)
                        else:
                            Q.append(v)
                        edges.remove([u, v])

        return False not in visitedStatus[1:]


print(Solution().findRedundantConnection(
      [[1, 2], [1, 3], [2, 3]]))
