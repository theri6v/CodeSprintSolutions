class Solution:
    def noOfWays(self, m, n, x):
        dp = [[0] * (x + 1) for _ in range(n + 1)]
        dp[n][0] = 1

        for i in range(n - 1, -1, -1):
            for tar in range(x + 1):
                dp[i][tar] = sum(dp[i + 1][tar - j] for j in range(1, m + 1) if tar - j >= 0)

        return dp[0][x]
