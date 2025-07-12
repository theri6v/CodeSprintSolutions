class Solution:
    def maxGold(self, mat):
        n=len(mat)
        m=len(mat[0])
        for j in range(1,m):
            for i in range(n):
                a=mat[i][j-1]
                b=mat[i-1][j-1] if i>0 else 0
                c=mat[i+1][j-1] if i<n-1 else 0
                mat[i][j]+=max(a,b,c)
        res=0
        j=m-1
        for i in range(n):
            res=max(res,mat[i][j])
        return res
