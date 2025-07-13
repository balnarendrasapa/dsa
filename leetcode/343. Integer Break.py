class Solution:
    def integerBreak(self, n: int) -> int:
        remainder = n % 3
        dividend = n // 3

        if n == 2:
            return 1

        if n == 3:
            return 2

        if remainder == 1:
            dividend -= 1
            return (3 ** dividend) * 4

        if remainder == 2:
            return (3 ** dividend) * 2

        if remainder == 0:
            return 3 ** dividend
