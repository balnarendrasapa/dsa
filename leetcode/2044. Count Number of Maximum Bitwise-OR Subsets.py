class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dp = Counter([0])

        for a in nums:
            for k, v in list(dp.items()):
                dp[k | a] += v

        return dp[max(dp)]
