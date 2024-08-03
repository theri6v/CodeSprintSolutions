class Solution:
    def celebrity(self, mat):
        n = len(mat)
        left, right = 0, n - 1
    
    # Step 1: Find the potential celebrity using two pointers
        while left < right:
            if mat[left][right] == 1:
                left += 1
            else:
                right -= 1
    
        potential_celebrity = left
    
    # Step 2: Verify the potential celebrity
        for i in range(n):
            if i != potential_celebrity:
                if mat[potential_celebrity][i] == 1 or mat[i][potential_celebrity] == 0:
                    return -1
    
        return potential_celebrity
        # code here
