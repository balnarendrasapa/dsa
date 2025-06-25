import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        res = ""
        for i in s:
            if i not in string.punctuation:
                res += i

        if res == res[::-1]:
            return True

        return False
