import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        left = []
        right = []

        i, j = 0, len(costs) - 1
        tc = 0

        while k > 0:
            while len(left) < candidates and i <= j:
                heapq.heappush(left, costs[i])
                i += 1

            while len(right) < candidates and i <= j:
                heapq.heappush(right, costs[j])
                j -= 1

            l = left[0] if left else float("inf")
            r = right[0] if right else float("inf")

            if l <= r:
                tc += l
                heapq.heappop(left)
            else:
                tc += r
                heapq.heappop(right)

            k -= 1
        
        return tc
