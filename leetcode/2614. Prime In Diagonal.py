class Solution:
    def isPrime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
        
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n = len(nums)
        diagonals = set()

        for i in range(n):
            diagonals.add(nums[i][i])
            diagonals.add(nums[i][n - 1 - i])

        m = 0
        for num in diagonals:
            if self.isPrime(num):
                m = max(m, num)

        return m
