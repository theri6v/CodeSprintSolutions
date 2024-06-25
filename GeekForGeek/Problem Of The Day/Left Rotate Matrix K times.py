class Solution:
    def rotateMatrix(self, k, mat):
        # code here
        res=[]
        m,n=len(mat),len(mat[0])
        for i in range(n):
            temp=[]
            for j in range(m):
                temp.append(mat[j][i])
            res.append(temp)
        k=k%len(res)
        while k:
            temp=res[0]
            res.pop(0)
            res.append(temp)
            k-=1
        for i in range(n):
            temp=[]
            for j in range(m):
                mat[j][i]=res[i][j]
        return mat
