class Solution:
    def countWays(self, s1 : str, s2 : str) -> int:
        def dfs(m,n):
            if n<0:
                return 1
            if m<0:
                return 0
            if dp[m][n]!=-1:
                return dp[m][n]
            if s1[m]==s2[n]:
                dp[m][n] = (dfs(m-1, n-1)+dfs(m-1, n))%MOD
                return dp[m][n]
            dp[m][n] = dfs(m-1, n)%MOD
            return dp[m][n]
        MOD=10**9+7
        dp = [[-1 for _ in range(len(s2)+1)]for _ in range(len(s1)+1)]
        return dfs(len(s1)-1, len(s2)-1)
