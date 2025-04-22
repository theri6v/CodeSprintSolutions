class Solution:
    def findUnique(self, arr):
        # code here 
        res=0
        for num in arr:
           res^=num
        return res
        
