#User function Template for python3
from collections import deque
class Solution:
    def numIslands(self, grid):
        # code here
        if not grid:
            return 0

        n, m = len(grid), len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        
        # Directions for moving in 8 directions
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # Up, Down, Left, Right
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonals
        ]
        
        def bfs(start_row, start_col):
            queue = deque([(start_row, start_col)])
            visited[start_row][start_col] = True
            
            while queue:
                row, col = queue.popleft()
                
                # Check all 8 directions
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    
                    # Check if the new cell is valid
                    if (0 <= new_row < n and 0 <= new_col < m 
                            and not visited[new_row][new_col] 
                            and grid[new_row][new_col] == 1):  # Change '1' to 1
                        visited[new_row][new_col] = True
                        queue.append((new_row, new_col))
        
        island_count = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:  # Change '1' to 1
                    bfs(i, j)
                    island_count += 1  # Increment island count
        
        return island_count
