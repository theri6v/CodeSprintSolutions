#User function Template for python3

class Solution:
    def series(self, n):
        if n==0:
            return [0]
        a=[0,1]
        for i in range(2,n+1):
            b=(a[i-1]+a[i-2])%((10**9)+7)
            a.append(b)
        return a
