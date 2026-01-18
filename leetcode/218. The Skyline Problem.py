class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []

        for l, r, h in buildings:
            events.append((l, -h))
            events.append((r, h))

        events.sort()

        result = []
        heap = [0]
        active = Counter({0: 1})
        prev_max = 0

        for x, h in events:
            if h < 0:
                heapq.heappush(heap, h)
                active[-h] += 1
            else:
                active[h] -= 1

            
            while heap and active[-heap[0]] == 0:
                heapq.heappop(heap)

            curr_max = -heap[0]
            if curr_max != prev_max:
                result.append([x, curr_max])
                prev_max = curr_max

        return result
