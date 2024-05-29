class Solution:
    def findWinner(self, n : int, x : int, y : int) -> int:
        # code here
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            if i >= 1 and dp[i - 1] == 0:
                dp[i] = 1
            elif i >= x and dp[i - x] == 0:
                dp[i] = 1
            elif i >= y and dp[i - y] == 0:
                dp[i] = 1
            else:
                dp[i] = 0

        return dp[n]
