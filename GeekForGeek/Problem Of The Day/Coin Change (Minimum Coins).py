class Solution:
    def fun(self,i, sum, coins, li):
        if sum == 0:
            return 0
        if sum < 0 or i == len(coins):
            return float('inf')
        
        if li[i][sum] != -1:
            return li[i][sum]
        
        take = float('inf')
        if coins[i] <= sum:
            take = self.fun(i, sum - coins[i], coins, li)
            if take != float('inf'):
                take += 1
        
        noTake = self.fun(i + 1, sum, coins, li)
        li[i][sum] = min(take, noTake)
        return li[i][sum]
        
    def minCoins(self, coins, sum):
        li = [[-1] * (sum + 1) for _ in range(len(coins))]
        ans = self.fun(0, sum, coins, li)
        return ans if ans != float('inf') else -1
