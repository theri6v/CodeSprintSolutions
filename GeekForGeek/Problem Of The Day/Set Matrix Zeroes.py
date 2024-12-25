#User function Template for python3
class Solution:
    def setMatrixZeroes(self, matrix):
        col0=1
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if(matrix[i][j]==0):
                    matrix[i][0]=0
                    if(j!=0):
                        matrix[0][j]=0
                    else:
                        col0=0
        for i in range(1,n):
            for j in range(1,m):
                if(matrix[i][0]==0 or matrix[0][j]==0):
                    matrix[i][j]=0
        if(matrix[0][0]==0):
            for i in range(1,m):
                matrix[0][i]=0
        for i in range(n):
            if(matrix[i][0]==0 or col0==0):
                matrix[i][0]=0
