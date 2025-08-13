import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        result = math.log(n, 3)

        return math.isclose(result, round(result), rel_tol=1e-15)
