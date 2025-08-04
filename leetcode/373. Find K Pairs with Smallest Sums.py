import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        heap = []
        result = []

        for i in range(len(nums2)):
            heapq.heappush(heap, [nums1[0] + nums2[i], 0, i])

        while k > 0 and heap:
            s, i, j = heapq.heappop(heap) 

            result.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1):
                heapq.heappush(heap, [nums1[i + 1] + nums2[j], i + 1, j])

            k -= 1

        return result
