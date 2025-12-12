class Solution:
    def transpose(self, mat):
        x = y = 0
        N = len(mat)
        
        while x < N:
            i, j = x + 1, y + 1
            
            while i < N:
                mat[i][y], mat[x][j] = mat[x][j], mat[i][y]
                i += 1
                j += 1
            
            x += 1
            y += 1
        
        return mat
        
