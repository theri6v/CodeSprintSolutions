#User function Template for python3

class Solution:
    
    def lcs(self,s1,s2,n1,n2):
        dp=[[None]*(n2+1) for _ in range(n1+1)]
        for i in range(n1+1):
            for j in range(n2+1):
                if i==0 or j==0:
                    dp[i][j]=0
                elif s1[i-1]==s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[n1][n2]
    
    def shortestCommonSupersequence(self, X, Y, m, n):
        return m+n-self.lcs(X,Y,m,n)
