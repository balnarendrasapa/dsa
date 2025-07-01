from collections import Counter

class Solution:
    def possibleStringCount(self, word: str) -> int:
        r = 0
        for i in range(1, len(word)):
            if word[i - 1] == word[i]:
                r += 1
        return r + 1
