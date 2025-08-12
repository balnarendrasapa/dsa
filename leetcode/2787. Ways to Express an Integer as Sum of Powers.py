class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        powers = []
        MOD = 10 ** 9 + 7

        i = 1
        while True:
            a = pow(i, x)

            if a > n:
                break

            powers.append(a)
            i += 1

        dp = [0 for _ in range(n + 1)]

        dp[0] = 1
        for p in powers:
            for i in range(n, p - 1, -1):
                dp[i] = (dp[i] + dp[i - p]) % MOD

        return dp[n]
