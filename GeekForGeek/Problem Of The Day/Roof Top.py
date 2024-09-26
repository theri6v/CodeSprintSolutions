#User function Template for python3

class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, arr):
        cs = 0
        maxi = 0
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                cs += 1
                maxi = max(maxi, cs)
            else:
                cs = 0
        
        return maxi
