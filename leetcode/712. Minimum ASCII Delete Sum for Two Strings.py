class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[j - 1] == s2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + ord(s1[j - 1])
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        total_ascii = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        return total_ascii - 2 * dp[n][m]
