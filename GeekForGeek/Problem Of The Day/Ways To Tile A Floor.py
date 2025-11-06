class Solution:
    def numberOfWays(self, n):
        # code here
        a=0
        b=1
        c=0
        for i in range(2,n+2):
            c=a+b
            a=b
            b=c
        return c
