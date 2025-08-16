import heapq
from collections import defaultdict

class Solution:          
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        incoming = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))
            incoming[v].append((u, w))

        heap = [(0, 0)]
        min_cost = [float("inf")] * n
        min_cost[0] = 0

        while heap:
            cost, node = heapq.heappop(heap)

            if node == n - 1:
                return cost

            if cost > min_cost[node]:
                continue

            for next_node, weight in graph[node]:
                new_weight = cost + weight
                if min_cost[next_node] > new_weight:
                    min_cost[next_node] = new_weight
                    heapq.heappush(heap, (new_weight, next_node))

            for prev_node, weight in incoming[node]:
                new_weight = cost + 2 * weight
                if min_cost[prev_node] > new_weight:
                    min_cost[prev_node] = new_weight
                    heapq.heappush(heap, (new_weight, prev_node))

        return -1
