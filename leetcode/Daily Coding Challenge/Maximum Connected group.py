from typing import List


class Solution:
    def MaxConnection(self, grid : List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return 0

        # Directions for top, bottom, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(x: int, y: int, comp_id: int) -> int:
            stack = [(x, y)]
            grid[x][y] = comp_id
            size = 0
            while stack:
                cx, cy = stack.pop()
                size += 1
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = comp_id
                        stack.append((nx, ny))
            return size

        component_sizes = {}
        comp_id = 2  # Start component IDs from 2 to differentiate from 1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = dfs(i, j, comp_id)
                    component_sizes[comp_id] = size
                    comp_id += 1

        max_size = max(component_sizes.values(), default=0)

        def get_adjacent_components(x: int, y: int) -> set:
            adjacent_components = set()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > 1:
                    adjacent_components.add(grid[nx][ny])
            return adjacent_components

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    adjacent_components = get_adjacent_components(i, j)
                    new_size = 1
                    for comp in adjacent_components:
                        new_size += component_sizes[comp]
                    max_size = max(max_size, new_size)

        return max_size
