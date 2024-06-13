#User function Template for python3

class Solution:
    def padovanSequence(self, n):
        if n<3 :
            return 1
        
        n1,n2,n3,sum=1,1,1,1
        mod=7+10**9
        
        for i in range(3,n+1):
            sum = (n1 + n2)%mod
            n1 = n2
            n2 = n3
            n3 = sum
        
        return sum
