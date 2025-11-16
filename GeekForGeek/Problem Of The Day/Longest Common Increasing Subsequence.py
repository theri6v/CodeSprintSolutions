class Solution:
    def LCIS(self, a, b):
        n, m = len(a), len(b)
        dp = [0] * m

        for i in range(n):
            currentMax = 0
            for j in range(m):

                if a[i] == b[j]:
                    dp[j] = currentMax + 1

                elif b[j] < a[i]:
                    currentMax = max(currentMax, dp[j])

        return max(dp)
