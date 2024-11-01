#User function Template for python3

class Solution:
    def maxSum(self,arr):
        n,ans=len(arr),0
        arr.sort()
        for i in range(n//2):
            ans-=(2*arr[i])
            ans+=(2*arr[n-1-i])
        return ans
