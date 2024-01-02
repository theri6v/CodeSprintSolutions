#User function Template for python3

class Solution():
    def maxSumWithK(self, a, n, k):
        # Code here
        dp = [0] * (n + 1)
        for i in range(n - 1,-1,-1):
            dp[i] = a[i] + dp[i + 1]
            dp[i] = max(dp[i],0)
        ans = float('-inf')
        total = 0
        for i in range(k):
            total += a[i]
        for i in range(k,n,1):
            ans = max(ans,total + dp[i])
            total += a[i]
            total -= a[i - k]
        return max(ans,total)
    
    
    
