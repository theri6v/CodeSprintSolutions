class Solution:
    # Function to find the maximum product subarray
    def maxProduct(self, arr):
        # Initialize variables
        max_product = arr[0]  # To store the final maximum product
        current_max = arr[0]  # Maximum product ending at the current position
        current_min = arr[0]  # Minimum product ending at the current position
        
        # Iterate through the array starting from the second element
        for i in range(1, len(arr)):
            num = arr[i]
            
            # If the current number is negative, swap current_max and current_min
            if num < 0:
                current_max, current_min = current_min, current_max
            
            # Update current_max and current_min
            current_max = max(num, num * current_max)
            current_min = min(num, num * current_min)
            
            # Update the overall maximum product
            max_product = max(max_product, current_max)
        
        return max_product
        # code here
        
