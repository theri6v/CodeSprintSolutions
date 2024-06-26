#User function Template for python3

class Solution:
    def findCoverage(self, matrix):
        count1=0
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    ## Check Up
                    if(i-1>=0 and matrix[i-1][j]==1):
                        count1+=1
                    ## Check Down
                    if(i+1<n and matrix[i+1][j]==1):
                        count1+=1
                    ## Check left
                    if(j-1>=0 and matrix[i][j-1]==1):
                        count1+=1
                    ## Check right
                    if(j+1<m and matrix[i][j+1]==1):
                        count1+=1
        return count1
