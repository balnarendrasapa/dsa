class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0

        n = len(prices)
        if k >= n // 2:
            profits = 0

            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    profits += prices[i] - prices[i - 1]

            return profits

        
        dp = [[0] * n for i in range(k + 1)]

        for t in range(1, k + 1):
            max_diff = -prices[0]
            for d in range(1, n):
                dp[t][d] = max(dp[t][d - 1], prices[d] + max_diff)
                max_diff = max(max_diff, dp[t - 1][d] - prices[d])

        return dp[k][n - 1]
