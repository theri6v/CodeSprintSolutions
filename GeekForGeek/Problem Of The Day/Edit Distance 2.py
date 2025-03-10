class Solution:
    def editDistance(self, s1, s2):
        # Code here
        n=len(s1)
        m=len(s2)
        res=[[float("inf")]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            res[i][m]=n-i
        for j in range(m+1):
            res[n][j]=m-j
        for k in range(n-1,-1,-1):
            for l in range(m-1,-1,-1):
                if s1[k]==s2[l]:
                    res[k][l]=res[k+1][l+1]
                else:
                    res[k][l]=min(res[k+1][l+1],res[k][l+1],res[k+1][l])+1
        return res[0][0]
                    
