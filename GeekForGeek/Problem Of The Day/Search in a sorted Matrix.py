#User function Template for python3
   # TC=O(n*m) & SC=O(1), Method1: Bruteforce, traverse the matrix using 2 loops
    # TC=O(n*log(m)) & SC=O(1), Method2: Better, in each row perform Binary search
    # TC=O(n + log(m)) ~= O(n), Method3: Optimal, Optimally traverse the matrix
    # Method3
class Solution:
    def searchMatrix(self, mat, x): 
        n, m = len(mat), len(mat[0])
        for vec in mat:
            if x < vec[0]: return False
            elif vec[0] <= x <= vec[m-1]:
                low, high = 0, m-1
                while low <= high:
                    mid = (low + high) // 2
                    if vec[mid] == x: return True
                    elif x > vec[mid]: low = mid + 1
                    else: high = mid - 1
        return False
        
