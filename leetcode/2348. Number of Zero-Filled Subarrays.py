class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        zero_count = [0 if i != 0 else 1 for i in nums]
        
        for i in range(1, len(zero_count)):
            if nums[i - 1] == nums[i] == 0:
                zero_count[i] = zero_count[i - 1] + 1

        return sum(zero_count)
