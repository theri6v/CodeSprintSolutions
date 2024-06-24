#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        if q<2 or q>2*n:
            return 0
        min_i=max(1,q-n)
        max_i=min(n,q-1)
        return max_i-min_i+1
