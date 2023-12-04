#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        diff=arr[n-1]-arr[0]
        for i in range(1, n):
            if(arr[i]-k<0):
                continue
            mini=min(arr[0]+k,arr[i]-k)
            maxi=max(arr[i-1]+k,arr[n-1]-k)
            diff=min(diff,maxi-mini)
        result = diff
        
        return result
