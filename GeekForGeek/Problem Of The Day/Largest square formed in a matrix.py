from typing import List

class Solution:
    def maxSquare(self, n: int, m: int, mat: List[List[int]]) -> int:
        dp = [0] * m
        maxsize = 0
        prev = 0

        for i in range(n):
            for j in range(m):
                temp = dp[j]
                if i == 0 or j == 0:
                    dp[j] = mat[i][j]
                elif mat[i][j] == 1:
                    dp[j] = min(dp[j], dp[j - 1], prev) + 1
                else:
                    dp[j] = 0
                maxsize = max(maxsize, dp[j])
                prev = temp

        return maxsize
