class Solution:
    def sequenceCount(self,s, t):
        dp = {}
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if j==len(t):
                return 1
            if i>=len(s) or j>=len(t):
                return 0
            if s[i]==t[j]:
                dp[(i, j)]= dfs(i+1, j+1)+dfs(i+1, j)
            else:
                dp[(i, j)]= dfs(i+1, j)
            return dp[(i, j)]%1000000007
        return dfs(0,0)%1000000007

