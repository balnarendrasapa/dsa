class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        count = 0
        while a or b or c:
            if a & 1 and not (c & 1):
                count += 1
            if b & 1 and not (c & 1):
                count += 1
            if not (a & 1) and not (b & 1) and c & 1:
                count += 1

            a >>= 1
            b >>= 1
            c >>= 1

        return count
