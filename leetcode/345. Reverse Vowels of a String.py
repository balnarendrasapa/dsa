class Solution:
    def reverseVowels(self, s: str) -> str:

        s = [i for i in s]
        i = 0
        j = len(s) - 1

        vowelset = {'a', 'e', 'i', 'o', 'u'}

        while i < j:
            if s[i].lower() not in vowelset:
                i += 1
            
            if s[j].lower() not in vowelset:
                j -= 1

            if s[i].lower() in vowelset and s[j].lower() in vowelset:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)
