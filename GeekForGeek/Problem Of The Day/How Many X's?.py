#User function Template for python3

class Solution:    
    def countX(self,L,R,X):
        res = 0
        for i in range(L + 1, R):
            res += str(i).count(str(X))
        return res

