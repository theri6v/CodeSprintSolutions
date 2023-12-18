#User function Template for python3
class Solution:
    def gameOfXor(self, N , A):
        ans=0
        for i,v in enumerate(A):
            if (i+1)*(N-i)%2==1:
                ans^=v
        return ans
