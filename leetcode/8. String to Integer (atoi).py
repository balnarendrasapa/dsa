class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()
        result = ""
        minus = False
        for j in range(len(s)):
            i = s[j]

            if (i == "-" or i == "+") and result == "" and len(s) >= 2 and (s[j + 1] == "+" or s[j + 1] == "-"):
                break

            if i == "-" and result == "":
                minus = True
                continue

            if i == "+" and result == "":
                continue

            if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                break
            else:
                result += i
        
        if result == "":
            return 0

        result = int(result)
        x = 2**31
        if minus == True:
            if -result < -x:
                result = x
            return -result
        else:
            if result > x - 1:
                result = x - 1
            return result
