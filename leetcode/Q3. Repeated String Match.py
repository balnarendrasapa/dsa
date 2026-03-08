class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = (len(b) // len(a))
        m = (len(b) // len(a) + 1)
        o = (len(b) // len(a) + 2)
        if b in a * n:
            return n
        elif b in a * m:
            return m
        elif b in a * o:
            return o
        return -1
