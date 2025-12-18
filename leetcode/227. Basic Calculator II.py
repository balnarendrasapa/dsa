class Solution:
    def calculate(self, s: str) -> int:
        operator = '+'
        num = 0
        stack = []
        s += '+'
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)

            elif c == " ":
                continue

            else:
                if operator == "+":
                    stack.append(num)
                elif operator == "-":
                    stack.append(-num)
                elif operator == "*":
                    operand = stack.pop()
                    stack.append(operand * num)
                elif operator == "/":
                    operand = stack.pop()
                    stack.append(int(operand / num))

                operator = c
                num = 0

        return sum(stack)
