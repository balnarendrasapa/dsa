class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for time in times:
            graph[time[0]].append((time[1], time[2]))

        que = [(0, k)]
        dist = {}
        while que:
            time, node = heapq.heappop(que)
            if node in dist:
                continue
            dist[node] = time
            for nex, ntime in graph[node]:
                if nex not in dist:
                    heapq.heappush(que, (time + ntime, nex))

        if len(dist) != n:
            return -1

        return max(dist.values())
