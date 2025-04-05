#User function Template for python3
from collections import deque

class Solution:
    def numIslands(self, grid):
        # code here
        r = len(grid)
        c = len(grid[0])
        visit = set()
        res = 0

        def bfs(i, j):
            q = deque()
            visit.add((i, j))
            q.append((i, j))
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1,1], [1, 1], [1, -1], [-1, -1]]
                for dr, dc in directions:
                    i = row + dr
                    j = col + dc
                    if (i in range(r)
                        and j in range(c)
                        and grid[i][j] == "L"
                        and (i, j) not in visit
                        ):
                            q.append((i, j))
                            visit.add((i, j))

        for i in range(r):
            for j in range(c):
                if grid[i][j] == "L" and (i, j) not in visit:
                    bfs(i, j)
                    res += 1
        return res

