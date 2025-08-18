#User function Template for python3
class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here
        citations.sort()
        c, res = 1, 0
        
        for cit in reversed(citations):
            res = max(res, min(cit, c))
            
            c += 1
        
        return res
