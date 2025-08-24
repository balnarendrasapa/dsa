class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        base26 = []

        for char in columnTitle:
            base26.append(ord(char) - ord("A") + 1)

        result = 0
        mul = 1
        for num in base26[::-1]:
            result += num * mul
            mul *= 26

        return result
