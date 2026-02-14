class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]

        while len(stones) > 1:
            heapq.heapify(stones)
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            if x != y:
                stones.append(y - x)

        return 0 if len(stones) == 0 else -stones[0]
