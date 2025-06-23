class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)

        if (0 not in nums1 and 0 not in nums2) and sum1 != sum2:
            return -1
        
        if sum1 == sum2 and 0 not in nums1 and 0 not in nums2:
            return sum1

        res1 = [i if i != 0 else 1 for i in nums1]
        res2 = [i if i != 0 else 1 for i in nums2]

        if sum(res1) > sum(res2) and 0 not in nums2:
            return -1

        if sum(res2) > sum(res1) and 0 not in nums1:
            return -1

        return max(sum(res1), sum(res2))
