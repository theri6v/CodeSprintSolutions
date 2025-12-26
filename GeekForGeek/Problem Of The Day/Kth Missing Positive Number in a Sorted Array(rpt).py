#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        # Initialize variables
        missing_count = 0
        prev = 0  # Previous number in the range
        
        # Traverse through the array
        for num in arr:
            # Count missing numbers between prev and num-1
            missing_in_gap = num - prev - 1
            if missing_count + missing_in_gap >= k:
                return prev + k - missing_count
            missing_count += missing_in_gap
            prev = num
        
        # If Kth missing number is beyond the array
        return prev + k - missing_count
