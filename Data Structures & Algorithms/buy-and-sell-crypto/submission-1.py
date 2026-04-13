class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                max_profit = prices[r] - prices [l]
                profit = max(profit, max_profit)
            else:
                l = r
            r += 1

        return profit