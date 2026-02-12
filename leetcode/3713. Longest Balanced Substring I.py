class Solution:
    def longestBalanced(self, s: str) -> int:
        m = 0
        for i in range(len(s)):
            t = ""
            f = dict()
            for j in range(i, len(s)):
                t += s[j]
                f[s[j]] = f.get(s[j], 0) + 1
                if len(set(f.values())) == 1:
                    m = max(m, len(t))

        return m
