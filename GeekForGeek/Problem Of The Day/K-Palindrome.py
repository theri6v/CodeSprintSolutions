#User function Template for python3

class Solution:
    def kPalindrome(self, str, n, k):
        # code here
        dp=[[None]*(n+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(n+1):
                if i==0 or j==0:
                    dp[i][j]=0
                elif str[i-1]==str[n-j]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return 1 if n-dp[n][n]<=k else 0
