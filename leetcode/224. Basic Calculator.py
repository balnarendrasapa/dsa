class Solution:
    def calculate(self, s: str) -> int:
        stack = [1]
        sign = 1
        result = 0
        i = 0
        n = len(s)

        while i < n:
            char = s[i]

            if char == ' ':
                i += 1
            elif char == '+':
                sign = stack[-1]
                i += 1
            elif char == '-':
                sign = -stack[-1]
                i += 1
            elif char == '(':
                stack.append(sign)
                i += 1
            elif char == ')':
                stack.pop()
                i += 1
            elif char.isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                result += sign * num
            else:
                i += 1  # just in case
        return result
