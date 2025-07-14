class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_array = [0] * n
        ma = -9999
        for j in range(n - 1, -1, -1):
            ma = max(ma, prices[j])
            max_array[j] = ma

        res_array = [0] * n

        for i in range(n - 1):
            res_array[i] = max_array[i + 1] - prices[i]

        return max(res_array)
