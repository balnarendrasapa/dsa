class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        one = 0
        two = 0
        res = []
        while one < len(nums1) and two < len(nums2):
            if nums1[one] > nums2[two]:
                res.append(nums2[two])
                two += 1
            else:
                res.append(nums1[one])
                one += 1
        if one < len(nums1):
            res.extend(nums1[one:])
        if two < len(nums2):
            res.extend(nums2[two:])
        if len(res) % 2 == 1:
            k = int(len(res) / 2)
            return res[k]
        else:
            k = int(len(res)/2)
            return (res[k] + res[k - 1]) / 2
