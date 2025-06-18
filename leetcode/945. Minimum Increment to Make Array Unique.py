class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()

        prev = -1
        result = 0

        for i in nums:

            if i <= prev:
                prev += 1
                result += prev - i
            else:
                prev = i
        
        return result
        
