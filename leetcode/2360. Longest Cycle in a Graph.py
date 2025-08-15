from collections import defaultdict

ACTIVE_NODE = 1
EXPLORED_NODE = 2

class Solution:
    def dfs(self, node, graph, visited, depth, heights):
        if node == -1:
            return 

        if visited[node] == ACTIVE_NODE:
            self.longest_cycle = max(self.longest_cycle, depth - heights[node])
            return

        if visited[node] == EXPLORED_NODE:
            return

        heights[node] = depth
        visited[node] = ACTIVE_NODE 

        self.dfs(graph[node][0], graph, visited, depth + 1, heights)
        visited[node] = EXPLORED_NODE

    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        graph = defaultdict(list)
        heights = defaultdict(int)
        self.longest_cycle = -1

        for i in range(n):
            graph[i].append(edges[i])

        visited = [0 for _ in range(n)]

        for node in graph.keys():
            if visited[node] == 0:
                self.dfs(node, graph, visited, 0, heights)

        return self.longest_cycle
