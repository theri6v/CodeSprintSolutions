from bisect import bisect_left
class Solution:
    def nonLisMaxSum(self, arr):
        LIS=[]
        liSum=[0]*(len(arr)+1)
        tot_sum=0
        for i in range(len(arr)):
            tot_sum+=arr[i]
            idx=bisect_left(LIS,arr[i])
            if idx==len(LIS):
                LIS.append(arr[i])
            else:
                LIS[idx]=arr[i]
            liSum[idx+1]=liSum[idx]+arr[i]
        return tot_sum-liSum[len(LIS)]

