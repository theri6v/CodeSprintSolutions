#User function template for Python

class Solution:
    def rectanglesInCircle(self, r: int) -> int:
        ans = 0
        for i in range(1, 2 * r):
            for j in range(1, 2 * r):
                if i * i + j * j <= 4 * r * r:
                    ans += 1
        return ans
