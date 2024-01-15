from typing import List


class Solution:
    def max_courses(self, n, total, cost):
        dp = [[0] * (total + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(total + 1):
                take, notake = 0, 0

                notake = dp[i + 1][j]

                if cost[i] <= j:
                    rem = j - cost[i] + (cost[i] * 9) // 10
                    take = 1 + dp[i + 1][rem]

                dp[i][j] = max(take, notake)

        return dp[0][total]
        
