#User function Template for python3

class Solution:
    #Function to find sum of all possible substrings of the given string.
    def sumSubstrings(self,s):
        res=0
        mod=10**9+7
        t=0
        for i in range(len(s)):
            val=int(s[i])
            t=((t*10)+val*(i+1))%mod
            res=(res+t)%mod
        return res
        
