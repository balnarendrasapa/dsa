class Solution:
    def reverseBits(self, n: int) -> int:
        x = str(bin(n))
        x = x[2:]
        add_zeroes = 32 - len(x)
        x = "0" * add_zeroes + x
        x = x[::-1]
        return int(x, 2)
