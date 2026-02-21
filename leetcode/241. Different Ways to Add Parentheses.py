class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}

        def dfs(expression):
            if expression in memo:
                return memo[expression]

            result = []
            for i, char in enumerate(expression):
                if char in "+-*":
                    left = dfs(expression[:i])
                    right = dfs(expression[i + 1:])

                    for l in left:
                        for r in right:
                            if char == "+":
                                result.append(l + r)
                            elif char == "-":
                                result.append(l - r)
                            else:
                                result.append(l * r)

            if not result:
                result.append(int(expression))

            return result

        return dfs(expression)
