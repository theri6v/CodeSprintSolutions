#User function Template for python3

class Solution:
    def FindExitPoint(self, n, m, matrix):
        direction = [0, 1]
        row, col = 0, 0
        while True:
            if matrix[row][col] == 1:
                if direction == [0, 1]:
                    direction = [1, 0]
                elif direction == [1, 0]:
                    direction = [0, -1]
                elif direction == [0, -1]:
                    direction = [-1, 0]
                elif direction == [-1, 0]:
                    direction = [0, 1]
                matrix[row][col] = 0
            
            nrow = row + direction[0]
            ncol = col + direction[1]
            
            if nrow >= n or nrow < 0 or ncol >= m or ncol < 0:
                return [row, col]
            
            row = nrow
            col = ncol
