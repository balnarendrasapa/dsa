from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dp = Counter(p)
        indices = []
        p_len = len(p)
        for i in range(len(s) - p_len + 1):
            temp = s[i:i + p_len]
            if Counter(temp) == dp:
                indices.append(i)

        return indices
