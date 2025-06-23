class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        ma = -999
        size = 0
        for i in nums:
            if i >= ma:
                ma = i
                size += 1

        return size
