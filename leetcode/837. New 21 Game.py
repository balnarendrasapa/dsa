class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts - 1:
            return 1

        dp = [0.0 for _ in range(n + 1)]
        dp[0] = 1.0

        window_sum = 1.0

        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts

            if i < k:
                window_sum += dp[i]

            if i >= maxPts:
                if i - maxPts < k:
                    window_sum -= dp[i - maxPts]

        return sum(dp[k:n+1])

        
