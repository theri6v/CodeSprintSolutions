class Solution:
    def distinctSubseq(self, s):
        mod = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        last = [-1] * 26
        
        dp[0] = 1
        
        for i in range(1, n + 1):
            dp[i] = (dp[i - 1] * 2) % mod
            c = ord(s[i - 1]) - 97
            if last[c] != -1:
                dp[i] = (dp[i] - dp[last[c] - 1] + mod) % mod
            last[c] = i
        
        return dp[n]
