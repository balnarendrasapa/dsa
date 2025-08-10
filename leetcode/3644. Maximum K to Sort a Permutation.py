from collections import defaultdict

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        
        res = -1

        for i, num in enumerate(nums):
            if i != num:
                if res == -1:
                    res = num
                else:
                    res &= num

        return res if res != -1 else 0
