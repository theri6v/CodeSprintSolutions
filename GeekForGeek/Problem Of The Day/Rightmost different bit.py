#User function Template for python3
class Solution:
    
    #Function to find the first position with different bits.
    def posOfRightMostDiffBit(self,m,n):
        #Your code here
        s = bin(m)
        a = bin(n)
        s=s[::-1]
        a=a[::-1]
        for i in range(min(len(s), len(a))):
            if s[i]!=a[i] :
                return i+1
        return -1
