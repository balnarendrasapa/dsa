class Solution:
    from collections import defaultdict
    
    def findDuplicate(self, nums: List[int]) -> int:
        temp = defaultdict(int)

        for i in nums:
            if temp[i] + 1 > 1:
                return i
            else:
                temp[i] += 1
