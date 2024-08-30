class Solution:
    def nQueen(self, n):
        # code here
        mat=[0]*n
        def check(mat,ind):
            i=ind-1
            while i>-1:
                if mat[i]==mat[ind] or mat[ind]-mat[i]==ind-i or mat[ind]-mat[i]==i-ind:
                    return False
                i-=1
            return True
            
        def rec(ind,mat,n):
            if ind==n:
                ans.append(mat.copy())
                return
            for i in range(n):
                mat[ind]=i+1
                if check(mat,ind):
                    mat[ind]=i+1
                    rec(ind+1,mat,n)
                    # print(mat)
                # mat[ind]=0    
        ans=[]
        rec(0,mat,n)
        return ans
