def factorial(n):
    if n == 0 or n == 1:
        return 1

    dp = []
    for i in range(n + 1):
        if i == 0 or i == 1:
            dp.append(1)
        
        dp.append(dp[-1] * i)

    return dp[-1]

def getPermutation_temp(n, k, numSet, result = ''):

    if n == 0:
        return result

    temp = factorial(n - 1)
    rem = k % temp
    dividend = k // temp

    if n == 1 and k == 1:
        result += str(numSet[0])
        return result

    if rem == 0:
        result += str(numSet[dividend - 1])
        numSet.pop(dividend - 1)
        return getPermutation_temp(n - 1, rem, numSet, result)

    else:
        result += str(numSet[dividend])
        numSet.pop(dividend)
        return getPermutation_temp(n - 1, rem, numSet, result)

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numSet = list(range(1, n + 1))

        return getPermutation_temp(n, k, numSet)
