#User function Template for python3
class Solution:
    def countgroup(self,arr): 
        ans = 0
        for i in arr:
            ans ^= i  
        
        if ans == 0:
            return pow(2, len(arr) - 1) - 1
        return 0

