class Solution:
    def maximumProfit(self, prices):
        # code here
        if not prices or len(prices) < 2:
            return 0  
        min_price = float('inf')  
        max_profit = 0  

        for price in prices:
            
            min_price = min(min_price, price)
            
            max_profit = max(max_profit, price - min_price)

        return max_profit
