#User function Template for python3

class Solution:
    def findWinner(self, n, A):
        # code here
        x0r = 0;
        for i in range(n):    
            x0r ^= A[i];
        return ((n % 2) + 1 if x0r else 1);
