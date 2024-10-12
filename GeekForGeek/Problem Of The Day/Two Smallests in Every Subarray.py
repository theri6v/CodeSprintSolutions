class Solution:
    def pairWithMaxSum(self, arr):
        
        if len(arr) < 2:
            return -1
        
        max_sum = 0

        for i in range(len(arr)-1):
            max_sum = max(max_sum, arr[i] + arr[i + 1])
    
        return max_sum 

                
            
        
