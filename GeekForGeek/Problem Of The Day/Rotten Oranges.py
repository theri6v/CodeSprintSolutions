import collections
class Solution:

    #Function to find minimum time required to rot all oranges. 
    def orangesRotting(self, grid):
        n, m = len(grid), len(grid[0])
        fresh = 0
        q = collections.deque()  # Use collections.deque for efficient popping from both ends
        dx = (-1, +1, 0, 0)
        dy = (0, 0, -1, +1)
        
        # Initialize the queue with rotten oranges and count fresh oranges
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        
        max_time = 0
        
        while q:
            i, j, level = q.popleft()  # Pop from the left for BFS
            
            for k in range(4):
                ip = i + dx[k]
                jp = j + dy[k]
                
                if 0 <= ip < n and 0 <= jp < m and grid[ip][jp] == 1:
                    grid[ip][jp] = 2  # Mark the orange as rotten
                    q.append((ip, jp, level + 1))
                    fresh -= 1
                    max_time = level + 1  # Update the maximum time
                    
        if fresh == 0:
            return max_time
        else:
            return -1

