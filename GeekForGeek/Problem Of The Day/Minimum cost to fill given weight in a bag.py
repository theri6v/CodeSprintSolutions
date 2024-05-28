
from typing import List



class Solution:
    def minimumCost(self, n : int, w : int, cost : List[int]) -> int:
        dp = [float('inf')] * (w + 1);
        dp[0] = 0
        
        for i in range(n):
            for j in range(i + 1, w + 1):
                dp[j] = min(dp[j], cost[i] + dp[j - i - 1])
            
        return dp[w]
        

