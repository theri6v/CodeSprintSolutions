#User function Template for python3
class Solution:
    def minimizeCost(self, k, arr):
        # code here
        n = len(arr)
        dp = [float('inf')] * n
        dp[0] = 0  # Starting point
        
        for i in range(n):
            for j in range(i + 1, min(i + k + 1, n)):
                dp[j] = min(dp[j], dp[i] + abs(arr[i] - arr[j]))
        
        return dp[n - 1]
