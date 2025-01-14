# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        
        # Calculate the total sum of the array.
        total_sum = sum(arr)
        
        # Initialize left_sum to 0.
        left_sum = 0
        
        # Traverse the array to find the equilibrium point.
        for i in range(len(arr)):
            # Calculate right_sum as total_sum - left_sum - arr[i].
            right_sum = total_sum - left_sum - arr[i]
            
            # Check if left_sum is equal to right_sum.
            if left_sum == right_sum:
                return i  # Return the index if equilibrium point is found.
            
            # Update left_sum by adding the current element.
            left_sum += arr[i]
        
        # Return -1 if no equilibrium point exists.
        return -1
