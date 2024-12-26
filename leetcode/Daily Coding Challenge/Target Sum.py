class Solution:
  def findTargetSumWays(self, nums: list[int], target: int) -> int:
    summ = sum(nums)
    if summ < abs(target) or (summ + target) % 2 == 1:
      return 0

    def knapsack(target: int) -> int:
      # dp[i] := the number of ways to sum to i by nums so far
      dp = [1] + [0] * summ

      for num in nums:
        for j in range(summ, num - 1, -1):
          dp[j] += dp[j - num]

      return dp[target]

    return knapsack((summ + target) // 2)

---------------------------------------------------------------------------------------------------------------------

class Solution:
  def findTargetSumWays(self, nums: list[int], target: int) -> int:
    summ = sum(nums)
    if summ < abs(target) or (summ + target) % 2 == 1:
      return 0

    def knapsack(nums: list[int], target: int) -> int:
      # dp[i] := the number of ways to sum to i by nums so far
      dp = [0] * (target + 1)
      dp[0] = 1

      for num in nums:
        for i in range(target, num - 1, -1):
          dp[i] += dp[i - num]

      return dp[target]

    return knapsack(nums, (summ + target) // 2)
