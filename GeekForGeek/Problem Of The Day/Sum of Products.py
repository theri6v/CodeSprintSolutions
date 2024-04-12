#User function Template for python3

class Solution:
    def pairAndSum(self, n, arr):
        res= 0
        for i in range(32):
            count = 0
            for j in arr:
                if (1<<i)&  j!= 0:
                    count=count+ 1
            res += 2**i*count*(count-1)//2
        return res 
