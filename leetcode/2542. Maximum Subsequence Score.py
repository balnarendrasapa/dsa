import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        t = sorted(list(zip(nums1, nums2)), key = lambda x: -x[1])
        heap = []
        
        total = 0
        res = float("-inf")
        for a, b in t:
            total += a
            heapq.heappush(heap, a)

            if len(heap) > k:
                total -= heapq.heappop(heap)
            if len(heap) == k:
                res = max(res, total * b)

        return res
