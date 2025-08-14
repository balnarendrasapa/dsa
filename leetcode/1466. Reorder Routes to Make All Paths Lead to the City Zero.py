from collections import defaultdict

class Solution:   
    def search(self, city, graph, visited):
        visited[city] = True
        count = 0

        for neighbor, needs_reverse in graph[city]:
            if not visited[neighbor]:
                count += needs_reverse
                count += self.search(neighbor, graph, visited)
        return count

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        visited = [False for _ in range(n)]

        return self.search(0, graph, visited)
