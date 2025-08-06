from collections import deque

class Solution:
    def dfs(self, node, dest, graph, vis, ans, temp):
        if node in vis:
            return

        vis.add(node)
        if node == dest:
            ans[0] = temp
            return

        for n, v in graph[node].items():
            self.dfs(n, dest, graph, vis, ans, temp * v)


    def getGraph(self, equations, values):
        graph = {}

        for i in range(len(equations)):
            numerator = equations[i][0]
            denominator = equations[i][1]

            if numerator not in graph:
                graph[numerator] = {}

            if denominator not in graph:
                graph[denominator] = {}

            graph[numerator][denominator] = values[i]
            graph[denominator][numerator] = 1 / values[i]

        return graph


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.getGraph(equations, values)

        finalAnswer = []
        for query in queries:
            numerator = query[0]
            denominator = query[1]

            if numerator not in graph or denominator not in graph:
                finalAnswer.append(-1.0)
            else:
                vis = set()
                ans = [-1.0]
                temp = 1.0
                self.dfs(numerator, denominator, graph, vis, ans, temp)
                finalAnswer.append(ans[0])

        return finalAnswer



