class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(rocks)

        if sum(rocks) + additionalRocks >= sum(capacity):
            return n

        remaining = [capacity[i] - rocks[i] for i in range(n)]

        remaining.sort()

        count = 0
        tracker = 0
        for i in remaining:
            tracker += i
            if tracker > additionalRocks:
                break
            count += 1

        return count
