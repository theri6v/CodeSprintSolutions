class Solution:
    def rowWithMax1s(self, arr):
        n=len(arr)
        m=len(arr[0])
        ans=-1
        col=m-1
        for i in range(n):
            if arr[i][col]==1:
                ans=i
                while col>=0 and arr[i][col]==1:
                    col-=1
            if col<0:
                return ans
        return ans
