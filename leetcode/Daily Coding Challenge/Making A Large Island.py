from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def find_root(x):
            if parents[x] != x:
                parents[x] = find_root(parents[x])  # Path compression
            return parents[x]
        
        def union(x, y):
            root_x, root_y = find_root(x), find_root(y)
            if root_x != root_y:
                parents[root_x] = root_y
                set_sizes[root_y] += set_sizes[root_x]
        
        n = len(grid)
        parents = list(range(n * n))
        set_sizes = [1] * (n * n)
        
        # Build sets for existing islands
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    for dx, dy in [(-1, 0), (0, -1)]:  # Only check left and top
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj]:
                            union(i * n + j, ni * n + nj)
        
        max_island = max(set_sizes, default=0)
        
        # Check converting each 0 to 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen_roots = set()
                    new_size = 1
                    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj]:
                            root = find_root(ni * n + nj)
                            if root not in seen_roots:
                                seen_roots.add(root)
                                new_size += set_sizes[root]
                    max_island = max(max_island, new_size)
        
        return max_island
