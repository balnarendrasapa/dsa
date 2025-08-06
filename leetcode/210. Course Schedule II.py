class Solution:
    def dfs(self, i, pre_d, courses, visited):
        if i in courses:
            return True

        if i not in pre_d:
            courses.append(i)
            return True

        if visited[i]:
            return False

        visited[i] = True
        for j in pre_d[i]:
            if not self.dfs(j, pre_d, courses, visited):
                return False

        courses.append(i)
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = []

        pre_d = {}

        for i, j in prerequisites:
            pre_d[i] = pre_d.get(i, []) + [j]

        for i in range(numCourses):
            visited = [False for i in range(numCourses)]
            if not self.dfs(i, pre_d, courses, visited):
                return []

        return courses
