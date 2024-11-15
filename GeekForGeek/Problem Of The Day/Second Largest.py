#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        if len(arr) < 2:
            return -1  # Not enough elements for a second largest

        # Initialize variables
        largest = getSecondLargest = float('-inf')

        # Find the largest element
        for num in arr:
            if num > largest:
                largest = num

        # Find the second largest element
        for num in arr:
            if num > getSecondLargest and num < largest:
                getSecondLargest = num

        # Return the second largest, or -1 if it doesn't exist
        return getSecondLargest if getSecondLargest != float('-inf') else -1
        
    
