#User function Template for python3

class Solution:

    def nthPoint(self, n):

        MOD = 10**9 + 7
        if n == 0:
            return 1
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

        return dp[n]
