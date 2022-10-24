from typing import List


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        scores = {node: 0 for node in range(len(edges))}

        for i, edge in enumerate(edges):
            scores[edge] += i

        maxscore = max([score for score in scores.values()])
        keysWithMaxScore = [
            node for node in scores.keys() if scores[node] == maxscore]
        print(keysWithMaxScore)
        return min(keysWithMaxScore)


edges = [2, 0, 0, 2]
print(Solution().edgeScore(edges))
