from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]

        # Base case
        dp[0][0] = 0               # Not holding stock on day 0
        dp[0][1] = -prices[0]      # Bought stock on day 0

        for i in range(1, n):
            # Not holding: either do nothing or sell today
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            # Holding: either do nothing or buy today
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

        return dp[-1][0]  # Max profit without holding stock at end
