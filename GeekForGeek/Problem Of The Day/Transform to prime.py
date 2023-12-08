#User function Template for python3

import math

class Solution:
    def minNumber(self, arr,n):
        # code here
        sm=sum(arr)
        if sm==1:
            return 1
        def isprime(s):
            if s<=1:
                return False
            else:
                for i in range(2,int(math.sqrt(s))+1):
                    if s%i==0:
                        return False
                return True
                
        for i in range(sm,sm*sm+1):
            if isprime(i):
                return i-sm
