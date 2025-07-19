import math

def isPrime(n):
    if n <= 1:
        return False
        
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    div = int(math.sqrt(n)) + 1
    for i in range(3, div, 2):
        if n % i == 0:
            return False

    return True

class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0:
            return 0
            
        t = 0
        p = 0
        for i in range(n):
            t += nums[i]
            p += nums[i]
            if isPrime(i):
                p -= nums[i]
        
        return abs(2 * p - t)
        
        
