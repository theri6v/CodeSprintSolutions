#User function Template for python3

class Solution:
    def Maximize(self, arr): 
        # Complete the function
        mod=10**9+7
        arr.sort()
        s=0
        for i in range(len(arr)):
            s=(s+i*arr[i])%mod
        return s
            
      

