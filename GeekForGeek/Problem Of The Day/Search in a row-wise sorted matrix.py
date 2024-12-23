#User function Template for python3

class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x): 
        # code here 
        def searchInRow(row,x,n):
            l,r=0,n-1
            while l<=r:
                mid=(l+r)//2
                if row[mid]==x:
                    return True
                if row[mid]>=x:
                    r=mid-1
                else:
                    l=mid+1
            return False
        
        m,n=len(mat),len(mat[0])
        for k in range(m):
            if searchInRow(mat[k],x,n):
                return True
        return False
        
