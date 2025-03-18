# class Solution:
#     def equalPartition(self, arr):
#         # code here
class Solution:
    def equalPartition(self, arr: list[int]) -> bool:
        total_sum = sum(arr)
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        dp = [[False] * (target + 1) for _ in range(len(arr) + 1)]

        for i in range(len(arr) + 1):
            dp[i][0] = True

        for i in range(1, len(arr) + 1):
            for j in range(1, target + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[len(arr)][target]
