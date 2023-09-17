def find_pal(string, left, right):
    while left >= 0 and right <= len(string) - 1:
        if string[left] == string[right]:
            left -= 1
            right += 1
        else:
            break
    return string[left + 1:right]
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            substring1 = find_pal(s, i, i)
            substring2 = find_pal(s, i, i+1)
            if len(result) < len(substring1):
                result = substring1
            if len(result) < len(substring2):
                result = substring2
        return result            

        
