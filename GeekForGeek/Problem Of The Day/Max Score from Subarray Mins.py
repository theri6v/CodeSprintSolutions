class Solution:
    def maxSum(self, arr):
        ans = 0
        for i in range(len(arr)-1):
            ans=max(ans,arr[i]+arr[i+1])
        return ans
