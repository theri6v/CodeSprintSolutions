from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        
        price = prices
        
        n = len(price)
        
        if n < 2:
            return 0  # No profit if less than 2 prices available
    
        profit = 0
    
        # Traverse through the price array
        for i in range(1, n):
            # Add the profit from every profitable transaction
            if price[i] > price[i - 1]:
                profit += price[i] - price[i - 1]
    
        return profit
