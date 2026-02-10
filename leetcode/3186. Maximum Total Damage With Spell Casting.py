class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        c = Counter(power)
        sorted_power = sorted(c.keys())
        n = len(sorted_power)
        dp = [0] * n

        for i in range(n):
            prev_best = 0
            j = i - 1
            while j >= 0 and sorted_power[j] >= sorted_power[i] - 2:
                j -= 1
            
            if j >= 0:
                prev_best = dp[j]

            dp[i] = max(dp[i - 1], prev_best + sorted_power[i] * c[sorted_power[i]])

        return dp[-1]
