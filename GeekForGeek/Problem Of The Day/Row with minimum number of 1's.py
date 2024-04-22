#User function Template for python3

class Solution:
   def minRow(self,n,m,a):
        #code here
        b = []
        for row in a:
            b.append(sum(row))
        return b.index(min(b)) + 1
