import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()

        hp = []
        max_day = max(end for _, end in events)

        e_id = 0
        count = 0

        for day in range(1, max_day + 1):
            while e_id < len(events) and events[e_id][0] == day:
                heapq.heappush(hp, events[e_id][1])
                e_id += 1

            while hp and hp[0] < day:
                heapq.heappop(hp)

            if hp:
                heapq.heappop(hp)
                count += 1

        return count
