#User function Template for python3
class Solution:
    def countPairs(self, mat1, mat2, n, x):
        count=0
        i,j=0,0
        k,l=n-1,n-1
        while(i<n and k>=0):
            pair=mat1[i][j]+mat2[k][l]
            if pair==x:
                count+=1
                j+=1
                l-=1
            elif pair>x:
                l-=1
            else:
                j+=1
            if j==n:
                i+=1
                j=0
            if l==-1:
                k-=1
                l=n-1
        return count
                    
