class Solution:
    def maxSum(self, arr): 
        n = len(arr)
        
        # step 1: calculate sum array and initial value
        arrSum = sum(arr)
        currVal = 0
        for i in range(n):
            currVal += i * arr[i]
            
        maxVal = currVal
        
        # step 2: compute values for array notation
        for i in range(1, n):
            currVal = currVal + arrSum - n * arr[n - i]
            maxVal = max(maxVal, currVal)

        return maxVal
