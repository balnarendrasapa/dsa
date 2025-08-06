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
