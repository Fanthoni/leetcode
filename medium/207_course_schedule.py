from typing import Dict, List
from copy import deepcopy

# for every course in the graph
# check the requirements for this course, and check the requirements of that course etc...
# if this leads to course key 0 then this course is untakable


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.constructGraph(prerequisites)
        print(graph, "graph")

        if len(prerequisites) == 0:
            return True

        # Check if a cycle exists
        for course in graph.keys():
            prereq = [
                x for x in graph.keys() if course in graph[x]]

            i = 0
            while (i < len(prereq)):
                currCourse = prereq[i]
                # there are duplicates in prereq (cycle exists)
                if course in prereq or len(set(deepcopy(prereq))) != len(prereq):
                    return False
                prereq = prereq + (
                    [x for x in graph.keys() if currCourse in graph[x]])
                i += 1

        return True

    def constructGraph(self, arr: List[List[int]]) -> Dict:
        graph = {}

        for item in arr:
            course, prereq = item[0], item[1]
            if course not in graph.keys():
                graph[course] = set()
            graph[course].add(prereq)
        return graph


input = [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]
print(Solution().canFinish(8, input))
# print(Solution().countUniqueCourse([[1, 4], [2, 4], [3, 1], [3, 2]]))
