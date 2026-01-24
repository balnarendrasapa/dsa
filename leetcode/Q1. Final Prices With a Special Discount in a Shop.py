class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        n = len(prices)
        stack = []
        answer = [0] * n

        for i in range(n - 1, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()

            discount = stack[-1] if stack else 0

            answer[i] = prices[i] - discount

            stack.append(prices[i])

        return answer
