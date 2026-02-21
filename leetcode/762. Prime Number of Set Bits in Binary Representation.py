class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        c = 0
        for num in range(left, right + 1):
            set_count = bin(num).count('1')
            if set_count in primes:
                c += 1

        return c
