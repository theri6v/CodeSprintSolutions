class Solution:
    def rotateby90(self, mat):
        n = len(mat)
        for i in range(n):
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        for j in range(n):
            start = 0
            end = n - 1
            while start < end:
                mat[start][j], mat[end][j] = mat[end][j], mat[start][j]
                start += 1
                end -= 1
        return mat
