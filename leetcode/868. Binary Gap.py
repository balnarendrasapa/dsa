class Solution:
    def binaryGap(self, n: int) -> int:
        num = bin(n)[2:]
        m = 0
        prev = -1

        for i in range(len(num)):
            if num[i] == '1':
                if prev != -1:
                    m = max(m, i - prev)
                prev = i

        return m
