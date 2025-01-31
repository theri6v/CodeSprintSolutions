#User function Template for python3

class Solution:
    
    #Function to find a solved Sudoku. 
    def solveSudoku(self, mat):
        
        def isValid(mat,row,col,val):
            for i in range(9):
                if mat[i][col] == val or mat[row][i] == val:
                    return False
            start_row = row - row%3
            start_col = col - col%3
            for i in range(3):
                for j in range(3):
                    if mat[start_row+i][start_col+j] == val:
                       return False
            return True
        
        # Your code here
        ROWS = len(mat)
        COLS = len(mat[0])
        def solve(mat,r,c):
            if r==9:
                return True 
            if c == 9:
                return solve(mat,r+1,0)
            
            if mat[r][c]!=0:
                return solve(mat,r,c+1)
            for k in range(1,10):
                if isValid(mat,r,c,k):
                    mat[r][c] = k
                            
                    if solve(mat,r,c+1):
                      return True
                           
                    mat[r][c] = 0
               
            return False
        solve(mat,0,0)
        return mat
