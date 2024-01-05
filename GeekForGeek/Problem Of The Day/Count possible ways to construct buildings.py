#User function Template for python3

class Solution:
    def TotalWays(self, N):
        b= s = 1
        res = 0
        mod = 1000000007
        for i in range(N):
            res = (b%mod+s%mod)%mod
            b = s%mod
            s = res%mod
        return (res*res)%mod
