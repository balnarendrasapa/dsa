from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_t = {}
        t_s = {}

        for cs, ts in zip(s, t):
            if s_t.get(cs, ts) != ts or t_s.get(ts, cs) != cs:
                return False

            s_t[cs] = ts
            t_s[ts] = cs

        return True
