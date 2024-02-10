#User function Template for python3

class Solution:
    def numberOfPath (self, n, k, arr):
        # code here
        def f(i,j,s):
            if s > k:
                return 0
            if i==n-1 and j==n-1 and s+arr[i][j]==k:
                return 1
            if (i,j,s) in dp:
                return dp[(i,j,s)]
            left,right = 0,0
            if i+1 < n:
                left = f(i+1,j,s + arr[i][j])
            if j+1 < n:
                right = f(i,j+1,s + arr[i][j])
            
            dp[(i,j,s)] = left + right
            return dp[(i,j,s)]
        dp = {}
        return f(0,0,0)


