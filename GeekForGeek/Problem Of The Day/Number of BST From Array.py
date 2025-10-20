class Solution:
    def calc(self,arr,i,j):
        if j-i+1<=1:
            return 1
        ans = 0
        for k in range(i,j+1):
            ans += self.calc(arr,i,k-1)*self.calc(arr,k+1,j)
        return ans
            
    def countBSTs(self, arr):
        # Code here
        mp = {}
        n = len(arr)-1
        ans = [-1]*(n+1)
        for i in range(n+1):
            mp[arr[i]] = i
        
        arr.sort()
        for i in range(n+1):
             ans[mp[arr[i]]]=self.calc(arr,0,i-1)*self.calc(arr,i+1,n)
        return ans
