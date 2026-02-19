class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        removals = 0
        i = 0
        n = len(word)

        while i < n - 1:
            if abs(ord(word[i]) - ord(word[i + 1])) <= 1:
                removals += 1
                i += 2
            else:
                i += 1

        return removals
