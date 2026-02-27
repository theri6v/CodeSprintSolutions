class Solution:
    def countSquare(self, mat, x):
        n = len(mat)
        m = len(mat[0])
        
        # Step 1: Build Prefix Sum Matrix
        pre = [[0]*m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                pre[i][j] = mat[i][j]
                
                if i > 0:
                    pre[i][j] += pre[i-1][j]
                if j > 0:
                    pre[i][j] += pre[i][j-1]
                if i > 0 and j > 0:
                    pre[i][j] -= pre[i-1][j-1]
        
        count = 0
        
        # Step 2: Check all possible square sizes
        for size in range(1, min(n, m) + 1):
            for i in range(n - size + 1):
                for j in range(m - size + 1):
                    
                    r1, c1 = i, j
                    r2, c2 = i + size - 1, j + size - 1
                    
                    total = pre[r2][c2]
                    
                    if r1 > 0:
                        total -= pre[r1-1][c2]
                    if c1 > 0:
                        total -= pre[r2][c1-1]
                    if r1 > 0 and c1 > 0:
                        total += pre[r1-1][c1-1]
                    
                    if total == x:
                        count += 1
                        
        return count
