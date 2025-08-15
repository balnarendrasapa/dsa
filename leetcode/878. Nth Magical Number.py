import math

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        l = min(a, b)
        r = n * l
        MOD = 10 ** 9 + 7

        lcm = a * b / math.gcd(a, b)

        while l < r:
            mid = l + (r - l) // 2
            factor_count = mid // a + mid // b - mid // lcm

            if factor_count < n:
                l = mid + 1
            else:
                r = mid

        return l % MOD
