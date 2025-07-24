class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0 for _ in nums]

        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[0]
                
            if i == 1:
                dp[i] = max(nums[i], dp[i - 1])

            if i > 1:
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]
            
