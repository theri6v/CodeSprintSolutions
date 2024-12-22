#User function Template for python3
class Solution:
    def matSearch(self, mat, x):
        # Complete this function
        #O(m+n)
        
        n = len(matrix)
        m = len(matrix[0])
        
        row = 0
        col = m-1
        while row < n  and col >= 0:
            if mat[row][col] == x:
                return True
            
            if x > mat[row][col]:
                row += 1
            
            else:
                col -= 1
        return False
        
