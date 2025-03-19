class Solution:
    # References: https://www.youtube.com/watch?v=tuhjovVtDII
    def max_profit(self, prices, k, operation_no, index, memo):
        if operation_no == (2*k)+1 or index == len(prices):
            return 0 # 0 profit
            
        if memo[index][operation_no] != -1:
            return memo[index][operation_no]
        
        # If operation_no will odd then we have to buy 
        if operation_no % 2 !=0:
            # buy
            # two choice buy or not buy
            # If we buy then profit will decrease by buy price
            buy = -prices[index] + self.max_profit(prices, k, operation_no + 1, index + 1, memo) # Profit will decrease
            skip = 0 + self.max_profit(prices, k, operation_no, index + 1, memo) # No profit
            res = max(buy, skip)
            memo[index][operation_no] = res
            return res
        else:
            # Sale
            # two chioce sale or nto sale
            # If we sale then profit will added (we don't need to subtract because we already subtracted the selling price from profit during buying)
            sale = prices[index] + self.max_profit(prices, k, operation_no + 1, index + 1, memo)
            skip = 0 + self.max_profit(prices, k, operation_no, index + 1, memo) # No profit
            res = max(sale, skip)
            memo[index][operation_no] = res
            return res
                    
    
    def maxProfit(self, prices, k):
        # total operations is 2k because for one trasaction 2 operations are performed (buy and sale)
        rows = len(prices) + 1
        cols = 2*k + 1 # no of allowed transactions
        
        memo = [[-1]*cols for _ in range(rows)]
        
        return self.max_profit(prices, k, 1, 0, memo)
