from collections import defaultdict

class Solution:
    def appealSum(self, s: str) -> int:
        
        prev = [-1] * 26
        total = 0
        current = 0
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            current += i - prev[idx]
            prev[idx] = i
            total += current

        return total
