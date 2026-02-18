n = 10 ** 5
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
        for multiple in range(i * i, n + 1, i):
            is_prime[multiple] = False

primes = []
for i in range(2, n + 1):
    if is_prime[i]:
        primes.append(i)

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        c = 0

        p = 1
        for n in nums:
            p *= n

        for prime in primes:
            if p % prime == 0:
                c += 1

        return c
