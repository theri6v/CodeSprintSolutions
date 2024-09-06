#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        msum=arr[0]
        curr=0 
        for i in range(len(arr)):
            curr+=arr[i]
            msum=max(msum,curr)
            curr=max(curr,0)
        return(msum)
