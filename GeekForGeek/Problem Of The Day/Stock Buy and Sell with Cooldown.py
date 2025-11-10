class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0

        buy, sell, cool = -prices[0], 0, 0

        for i in range(1, n):
            prev_buy, prev_sell, prev_cool = buy, sell, cool
            buy = max(prev_buy, prev_cool - prices[i])
            sell = prev_buy + prices[i]
            cool = max(prev_cool, prev_sell)

        return max(sell, cool)
