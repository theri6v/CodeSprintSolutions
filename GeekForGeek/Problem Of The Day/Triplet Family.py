class Solution:
    def findTriplet(self, arr):
        # Sort the array to enable searching only in the remaining part of the array for each element
        arr.sort()
        n = len(arr)
        
        # Iterate through each unique pair (i, j)
        for i in range(n - 1):
            for j in range(i + 1, n):
                s = arr[i] + arr[j]
                # Use a hash set to check if the sum exists in the remaining elements
                if s in arr[j + 1:]:
                    return True
        return False
                
        
