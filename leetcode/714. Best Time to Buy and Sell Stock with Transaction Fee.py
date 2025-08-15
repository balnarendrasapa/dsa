class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = -prices[0]
        cash = 0

        for price in prices[1:]:
            cash = max(cash, price + hold - fee)
            hold = max(hold, cash - price)

        return cash
