class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left_array = [0 for i in prices]
        temp_min = prices[0]
        for i in range(1, len(prices)):
            temp_min = min(temp_min, prices[i])
            left_array[i] = max(left_array[i - 1], prices[i] - temp_min)

        right_array = [0 for i in prices]
        temp_max = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            temp_max = max(temp_max, prices[i])
            right_array[i] = max(right_array[i + 1], temp_max - prices[i])

        profits = [0 for i in prices]

        max_v = 0
        for i in range(len(profits)):
            max_v = max(max_v, left_array[i] + right_array[i])

        return max_v
