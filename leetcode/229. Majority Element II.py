from collections import Counter
import math

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        k = len(nums) // 3

        result = []
        for key, value in c.items():
            if value > k:
                result.append(key)

        return result
