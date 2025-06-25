from bisect import bisect_left, bisect_right
from math import ceil

def getCount(nums1, nums2, mid):
    count = 0
    for num in nums1:
        if num == 0:
            if mid >= 0:
                count += len(nums2)
        elif num > 0:
            temp = mid // num
            count += bisect_right(nums2, temp)
        else:
            temp = ceil(mid / num)
            count += len(nums2) - bisect_left(nums2, temp)
    return count


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        left = -10**10
        right = 10**10

        while left < right:
            mid = (left + right) // 2

            count = getCount(nums1, nums2, mid)
            if count < k:
                left = mid + 1
            else:
                right = mid

        return left
