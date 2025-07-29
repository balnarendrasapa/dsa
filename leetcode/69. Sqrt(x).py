class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        j = 1

        while True:
            if i * i == x:
                return i

            if j * j == x:
                return j

            if i * i < x < j * j:
                return i
            
            i += 1
            j += 1
