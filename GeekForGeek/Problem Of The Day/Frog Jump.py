class Solution:
    def minCost(self, height):
        n = len(height)
        if n == 1:
            return 0
        prev = 0
        prev2 = 0
        for i in range(1, n):
            jump1 = prev + abs(height[i] - height[i-1])
            jump2 = float('inf')
            if i > 1:
                jump2 = prev2 + abs(height[i] - height[i-2])
            curr = min(jump1, jump2)
            prev2 = prev
            prev = curr
        return prev
