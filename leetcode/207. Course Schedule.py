class Solution:
    def dfs(self, i, pre_d, courses, visited):
        if courses[i]:
            return True

        if i not in pre_d:
            courses[i] = True
            return True

        if visited[i]:
            return False

        visited[i] = True
        for j in pre_d[i]:
            if not self.dfs(j, pre_d, courses, visited):
                return False

        courses[i] = True
        return True
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courses = [False for i in range(numCourses)]

        pre_d = {}

        for i, j in prerequisites:
            pre_d[i] = pre_d.get(i, []) + [j]

        for i in range(numCourses):
            visited = [False for i in range(numCourses)]
            if not self.dfs(i, pre_d, courses, visited):
                return False

        return True

# from typing import List

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         # Build adjacency list
#         graph = [[] for _ in range(numCourses)]
#         for course, prereq in prerequisites:
#             graph[course].append(prereq)

#         # 0 = unvisited, 1 = visiting, 2 = visited
#         state = [0] * numCourses

#         def dfs(course):
#             if state[course] == 1:  # cycle detected
#                 return False
#             if state[course] == 2:  # already checked
#                 return True

#             state[course] = 1  # mark as visiting
#             for prereq in graph[course]:
#                 if not dfs(prereq):
#                     return False

#             state[course] = 2  # mark as visited
#             return True

#         for i in range(numCourses):
#             if not dfs(i):
#                 return False

#         return True

