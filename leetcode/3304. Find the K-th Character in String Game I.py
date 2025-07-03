def getString(word, k):
    
    if len(word) > k:
        return word
    else:
        temp = ""
        for c in word:
            temp += chr(ord(c) + 1)
        return getString(word + temp, k)
    

class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        return getString(word, k)[k - 1]
