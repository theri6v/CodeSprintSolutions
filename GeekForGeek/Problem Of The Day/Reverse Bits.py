#User function Template for python3

class Solution:
    def reversedBits(self, x):
        # code here 
        b=bin(x)[2:]
        l=len(b)
        z=32-l
        k=[]
        for i in range(z):
            k.append('0')
        
        c=''.join(k)
        r=c+b
        r=r[::-1]
        res=int(r,2)
        return res
        
