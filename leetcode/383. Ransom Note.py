from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)

        for c in c1.keys():
            if c not in c2.keys() or c1[c] > c2[c]:
                return False

        return True
        
