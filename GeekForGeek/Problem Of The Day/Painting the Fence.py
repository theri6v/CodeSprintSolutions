#User function Template for python3

class Solution:
    def countWays(self,n,k):
        #code here.
        total = k  
        diff = k 
        same = 0 
        mod = 10**9 + 7
        for i in range(2,n+1):
            same = diff
            diff = ((k-1)%mod*total%mod)%mod
            total = (same+diff)%mod 
            
        return total
