from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc = Counter(s)
        tc = Counter(t)

        if sc.keys() != tc.keys():
            return False
        else:
            for key in sc.keys():
                if sc[key] != tc[key]:
                    return False
            
            return True
