from typing import List


# Time Limit Exceeded
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        # get shortest path to Nth node from every node

        # total_restricted paths = 0
        # for every branch node that has lower diestance to last:
        #  total restricted +=  countRestrictedPaths(this node)
        # return total restricted paths
        graph = [([0] * n) for i in range(n)]

        for u, v, w in edges:
            graph[u-1][v-1] = w
            graph[v-1][u-1] = w
        weights = self.djikstra(graph, n-1)
        return self.countPath(0, graph, weights, n-1)

    def countPath(self, node, graph, weights, goal):
        if node == goal:
            return 1

        totalRestPaths = 0
        neighbourNodes = [i for i in range(
            0, len(graph)) if graph[i][node] != 0]
        for neighbour in neighbourNodes:
            if weights[neighbour] < weights[node]:
                totalRestPaths += self.countPath(
                    neighbour, graph, weights, goal)
        return totalRestPaths

    def djikstra(self, graph, x):
        shortest = {n: float("inf") for n in range(0, len(graph))}
        shortest[x] = 0
        Q = [x]

        while len(Q) <= len(shortest.keys()):
            currNodeToRelax = Q[-1]
            for i, node in enumerate(graph):
                if node[currNodeToRelax] != 0:
                    shortest[i] = min(
                        shortest[i], shortest[currNodeToRelax] + node[currNodeToRelax])
            notInQ = {node: shortest[node]
                      for node in shortest.keys() if node not in Q}
            if len(notInQ.keys()) > 0:
                Q.append(min(zip(notInQ.values(), notInQ.keys()))[1])
            else:
                return shortest


graph = [
    [0, 3, 3, 2, 0],
    [3, 0, 1, 0, 2],
    [3, 1, 0, 0, 1],
    [2, 0, 0, 0, 10],
    [0, 2, 1, 10, 0],
]
edges = [[1, 2, 3], [1, 3, 3], [2, 3, 1], [
    1, 4, 2], [5, 2, 2], [3, 5, 1], [5, 4, 10]]

print(Solution().countRestrictedPaths(5, edges))
