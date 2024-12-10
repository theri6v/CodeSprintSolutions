#User function Template for python3
class Solution:
    def minRemoval(self, intervals):
        # Sort intervals by their ending times
        intervals.sort(key=lambda x: x[1])
        
        # Initialize variables
        count = 0  # To count intervals that need to be removed
        prev_end = float('-inf')  # To track the end of the last added interval
        
        # Traverse through the intervals
        for start, end in intervals:
            if start >= prev_end:
                # No overlap, update prev_end
                prev_end = end
            else:
                # Overlapping interval, increment count
                count += 1
        
        return count
