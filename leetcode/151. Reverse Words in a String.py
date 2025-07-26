class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.strip()
        words = s.split(" ")
        result = ""
        for word in words[::-1]:
            if word != " " and word != "":
                result += word + " "

        return result.strip()
