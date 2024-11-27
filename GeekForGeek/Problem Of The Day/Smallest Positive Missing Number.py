#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr):
        n = len(arr)
    
        # Step 1: Rearrange numbers to their correct positions
        for i in range(n):
            while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
      
        # Step 2: Find the first missing positive number
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1
    
        # Step 3: Handle case where all numbers are in place
        return n + 1
