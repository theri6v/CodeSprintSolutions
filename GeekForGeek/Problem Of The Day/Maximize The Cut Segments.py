#User function Template for python3

class Solution:

    def cut(self, n, x, y, z, dp):
        if n < 0:
            return float('-inf')
        elif n == 0:
            return 0
        elif dp[n] != 0:
            return dp[n]
        cutx = self.cut(n-x, x, y, z, dp)
        cuty = self.cut(n-y, x, y, z, dp)
        cutz = self.cut(n-z, x, y, z, dp)
        dp[n] = 1 + max(cutx, max(cuty, cutz))
        return dp[n]
    
    def maximizeTheCuts(self, n, x, y, z):
        dp = [0] * (n + 1)
        result = self.cut(n, x, y, z, dp)
        return max(result, 0)

