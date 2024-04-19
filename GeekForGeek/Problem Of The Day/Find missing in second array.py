#User function Template for python3

class Solution:
    def findMissing(self,a,b,n,m):
    # code here
        ans = []
        k = set(b)
        
        for i in a:
            if i not in k:
                ans.append(i)
        return ans
