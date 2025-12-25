class Solution:
    def findPeakGrid(self, mat):
        n = len(mat)
        m = len(mat[0])
        arr = []
        for row in mat:
            arr.extend(row)
            
        maxi = max(arr)
        idx = arr.index(maxi)
        c = idx % m
        r = idx // m
        return [r, c]
