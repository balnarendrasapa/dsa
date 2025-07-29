class Solution:
    def trailingZeroes(self, n: int) -> int:
        div = 5
        res = 0
        while n // div != 0:
            res += n // div
            div *= 5
        return res
