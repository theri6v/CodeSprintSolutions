#User function Template for python3
class Solution:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr):
        if not arr:
            return 0
        
        inc = 1
        dec = 1
        
        # Traverse the array
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                inc = dec + 1
            elif arr[i] < arr[i - 1]:
                dec = inc + 1
        
        return max(inc, dec)

