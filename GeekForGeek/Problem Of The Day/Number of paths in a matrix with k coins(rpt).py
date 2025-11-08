class Solution:
    def numberOfPath(self, mat, k):
        # code here
        def f(i, j, s):
            if s > k:
                return 0
            if i == m-1 and j == n-1:
                s += mat[i][j]
                if s == k:
                    return 1
                return 0
            if i>=m or j>=n:
                return 0
            if (i, j, s) in dp:
                return dp[(i, j, s)]
            p1 = f(i+1, j, s+mat[i][j])
            p2 = f(i, j+1, s + mat[i][j])
            dp[(i, j, s)] = p1+p2
            return p1 + p2
        m, n = len(mat), len(mat[0])
        dp = {}
        return f(0,0,0)
