#User function Template for python3

class Solution:
    def determinantOfMatrix(self,matrix,n):
#        laplace/cofactor expansion
        def hlp(mat,n):
            if n==1:
                return mat[0][0]
            ans=0
            for i in range(n):
                if mat[0][i]==0:
                    continue
                sgn=1 if i%2==0 else -1
                nmat=[[rw[x] for x in range(n) if x!=i] for rw in mat[1:]]
                ans+=sgn*mat[0][i]*hlp(nmat,n-1)
            return ans
        return hlp(matrix,n)
