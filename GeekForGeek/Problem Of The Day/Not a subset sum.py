#User function Template for python3

class Solution:
    def findSmallest(self, arr):
        # code here
        smallest_missing = 1  # Start with the smallest positive integer
        
        for num in arr:
            if num > smallest_missing:
                break
            smallest_missing += num  # Update smallest_missing if num is usable
        
        return smallest_missing
