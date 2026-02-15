class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        c = 0
        for i in range(len(word)):
            if ord("A") <= ord(word[i]) <= ord("Z"):
                c += 1

        if len(word) == c:
            return True

        if c == 1 and ord("A") <= ord(word[0]) <= ord("Z"):
            return True

        if c == 0:
            return True

        return False
