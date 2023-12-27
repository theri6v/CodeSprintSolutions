#User function Template for python3

class Solution:
    def antiDiagonalPattern(self,matrix):
        # Code here
        ar=[]
        key=0
        n=len(matrix)
        for i in range((n-1)*2+1):
            for i in range(n):
                for j in range(n):
                    if i + j == key:
                        ar.append(matrix[i][j])
            key+=1
        return ar
