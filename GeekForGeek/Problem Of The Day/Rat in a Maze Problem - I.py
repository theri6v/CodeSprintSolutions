from typing import List

class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        # code here
        def is_safe(x, y):
            return 0 <= x < n and 0 <= y < n and m[x][y] == 1

        def dfs(x, y, path, visited):
            if not is_safe(x, y) or visited[x][y]:
                return
            if x == n - 1 and y == n - 1:
                paths.append(path)
                return
            visited[x][y] = True
            dfs(x + 1, y, path + 'D', visited)
            dfs(x - 1, y, path + 'U', visited)
            dfs(x, y + 1, path + 'R', visited)
            dfs(x, y - 1, path + 'L', visited)
            visited[x][y] = False

        n = len(m)
        if m[0][0] == 0 or m[n - 1][n - 1] == 0:
            return []
        paths = []
        visited = [[False for _ in range(n)] for _ in range(n)]
        dfs(0, 0, "", visited)
        return paths
