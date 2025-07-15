import string

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        digits = string.digits
        letters = string.ascii_letters
        vowels = "aeiouAEIOU"
        consonants = [i for i in letters if i not in vowels]

        flag1 = False
        flag2 = False
        for i in word:
            if i not in digits and i not in letters:
                return False

            if i in vowels:
                flag1 = True

            if i in consonants:
                flag2 = True

        if not flag1 or not flag2:
            return False

        return True

        
