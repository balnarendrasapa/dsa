class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        left = 0
        sum_value = 0
        ans = len(nums)
        for right, val in enumerate(nums):
            sum_value += val
            while sum_value >= target:
                sum_value -= nums[left]
                ans = min(ans, right - left + 1)
                left += 1
        
        return ans
