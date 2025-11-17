class Solution:
    def maxSumIS(self, arr):
        n = len(arr)
        dp, ans = arr[:], arr[0]
        
        for i in range(1, n):
            for j in range(i):
                if arr[i]>arr[j] and dp[i]<arr[i]+dp[j]:
                    dp[i] = arr[i]+dp[j]
            ans = max(ans, dp[i])
        
        return ans
