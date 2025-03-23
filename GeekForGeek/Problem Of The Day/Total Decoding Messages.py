#User function Template for python3
class Solution:
    def countWays(self, digits):
        n=len(digits)
        dp=[0]*(n+1)
        dp[0]=1
        for i in range(n):
            if digits[i]!='0':
                dp[i+1]+=dp[i]
            if i-1>=0 and digits[i-1]!='0' and int(digits[i-1:i+1])<=26:
                dp[i+1]+=dp[i-1]
        return dp[-1]
