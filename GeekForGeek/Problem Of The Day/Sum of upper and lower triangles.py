
#User function Template for python3


class Solution:
    
    #Function to return sum of upper and lower triangles of a matrix.
    def sumTriangles(self,matrix, n):
        # code here 
        l = []
        up=0
        do=0
        dg=0
        for i in range(n):
            for j in range(n):
                if i==j:
                    dg+=matrix[i][j]
                elif i<j:
                    up+=matrix[i][j]
                # elif i>j:
                else:
                    do+=matrix[i][j]
        upper=up+dg
        lower=do+dg
        l.append(upper)
        l.append(lower)
        return l
