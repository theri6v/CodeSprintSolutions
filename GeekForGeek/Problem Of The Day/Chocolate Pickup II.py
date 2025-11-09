class Solution:
    def chocolatePickup(self, grid):
        from functools import lru_cache

        n = len(grid)
        m = len(grid[0])

        @lru_cache(None)
        def dp(r1, c1, c2):
            r2 = r1 + c1 - c2
            if r1 >= n or c1 >= m or r2 >= n or c2 >= m or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')

            if r1 == n - 1 and c1 == m - 1:
                return grid[r1][c1]

            res = grid[r1][c1]
            if (r1, c1) != (r2, c2):
                res += grid[r2][c2]

            res += max(
                dp(r1 + 1, c1, c2 + 1),  # down, right
                dp(r1, c1 + 1, c2 + 1),  # right, right
                dp(r1 + 1, c1, c2),      # down, down
                dp(r1, c1 + 1, c2)       # right, down
            )
            return res

        result = dp(0, 0, 0)
        return max(0, result)
