import math

MOD = 10**9 + 7

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        if k >= n:
            return 0

        formula = m * pow(m - 1, n - (k + 1), MOD) % MOD

        combination = math.comb(n - 1, k) % MOD

        return formula * combination % MOD
