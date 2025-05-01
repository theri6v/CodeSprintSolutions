#User function Template for python3
class Solution:

    def nthRowOfPascalTriangle(self, n):
        # code here
        tri=[]
        for r in range(n):
            row=[1]*(r+1)
            for c in range(1,r):
                row[c]=tri[r-1][c-1]+tri[r-1][c]
            tri.append(row)
        return tri[n-1]     
