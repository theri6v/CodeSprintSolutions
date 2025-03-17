class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        def solve(ind,s):
            if(s==sum):
                return True
            if(ind==len(arr)):
                return False
            if((ind,s) in dp):
                return dp[(ind,s)]
            temp = solve(ind+1,s+arr[ind]) or solve(ind+1,s)
            return temp
            
            
        dp = [[False]*(sum+1) for i in range(len(arr)+1)]
        for i in range(len(arr)+1):
            dp[i][sum] = True
        for i in range(len(arr)-1,-1,-1):
            for j in range(sum,-1,-1):
                a = dp[i+1][j]
                if(j+arr[i]<=sum):
                    a|=dp[i+1][j+arr[i]]
                dp[i][j] = a
        return dp[0][0]
                
        
