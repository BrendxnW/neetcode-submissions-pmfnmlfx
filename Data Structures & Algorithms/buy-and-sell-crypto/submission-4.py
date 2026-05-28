class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 0
        profit = 0

        while sell < len(prices) and buy < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell

            else:
                temp_profit = prices[sell] - prices[buy]
                profit = max(profit, temp_profit)
            sell += 1

        return profit