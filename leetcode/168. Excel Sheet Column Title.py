class Solution:
    def get_base26(self, num):
        if num == 0:
            return 0

        digits = []

        while num > 0:
            num -= 1
            digits.append(num % 26)
            num //= 26

        return digits[::-1]

        
    def convertToTitle(self, columnNumber: int) -> str:
        
        result = ""

        for i in self.get_base26(columnNumber):
            result += chr(ord('A') + i)

        return result
