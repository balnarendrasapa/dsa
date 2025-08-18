from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = Counter(nums)

        t = list(c.keys())
        t.sort()
        dp = [0 for _ in t]

        dp[0] = c[t[0]] * t[0]

        for i in range(1, len(t)):
            points = c[t[i]] * t[i]
            if t[i] == t[i - 1] + 1:
                dp[i] = max(dp[i - 1], (dp[i - 2] + points if i - 2 >= 0 else points))
            else:
                dp[i] = dp[i - 1] + points

        return dp[-1]
