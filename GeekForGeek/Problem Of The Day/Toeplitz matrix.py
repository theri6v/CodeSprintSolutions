# You are required to complete this method
# Return True/False or 1/0
def isToeplitz(mat):
    #code here
    rows=len(mat)
    columns=len(mat[0])
    for i in range (1,rows):
        for j in range (1,columns):
            if  mat[i-1][j-1]!=mat[i][j]:
                return False
    return True 
