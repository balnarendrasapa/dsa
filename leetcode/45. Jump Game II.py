class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("inf")] * n
        dp[-1] = 0
        i = n - 2
        count = 0
        while i >= 0:
            element = nums[i]
            j = i + 1
            while j <= n - 1 and j <= i + element:
                if dp[j] != float('inf'):
                    dp[i] = min(dp[i], dp[j] + 1)
                j += 1
            i -= 1

        return dp[0]
