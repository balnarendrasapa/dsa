class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s

        start = 0
        count = 0
        parts = []

        for i, ch in enumerate(s):
            count += 1 if ch == '1' else -1
            if count == 0:
                middle = self.makeLargestSpecial(s[start + 1:i])
                parts.append('1' + middle + '0')
                start = i + 1

        parts.sort(reverse = True)

        return "".join(parts)
