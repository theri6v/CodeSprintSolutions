#User function Template for python3

class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        
        dp = []
        dp.append(Arr[0])
        for i in range(1,N):
            dp.append(dp[i-1]+Arr[i])
            
        res = []
        res.append(dp[K-1])
        
        for i in range(1,len(dp)):
            K +=1
            if K<len(dp):
                s = dp[K-1]-dp[i-1]
            else:
                s = dp[-1] - dp[i-1]
            res.append(s)
            
        res = max(res)
        return res
