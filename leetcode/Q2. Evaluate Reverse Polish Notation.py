class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                op2, op1 = int(stack.pop()), int(stack.pop())
                value = 0
                match token:
                    case "+":
                        value = op1 + op2
                    case "-":
                        value = (op1 - op2)
                    case "*":
                        value = op1 * op2
                    case "/":
                        value = op1 / op2
                
                stack.append(value)                
            else:
                stack.append(token)

        return int(stack[-1])
