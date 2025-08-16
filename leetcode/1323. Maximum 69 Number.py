class Solution:
    def maximum69Number (self, num: int) -> int:
        result = ""
        flag = False
        for char in str(num):
            if char == "9":
                result += char

            elif char == "6" and not flag:
                result += "9"
                flag = True
            
            else:
                result += char

        return int(result)
