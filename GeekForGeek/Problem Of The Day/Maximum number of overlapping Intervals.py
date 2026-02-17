class Solution:
    def overlapInt(self, arr):
        n = len(arr)
        
        # Separate start and end times
        start = []
        end = []
        
        for interval in arr:
            start.append(interval[0])
            end.append(interval[1])
        
        # Sort both arrays
        start.sort()
        end.sort()
        
        i = 0
        j = 0
        curr_overlap = 0
        max_overlap = 0
        
        # Sweep line technique
        while i < n and j < n:
            if start[i] <= end[j]:   # Inclusive overlap
                curr_overlap += 1
                max_overlap = max(max_overlap, curr_overlap)
                i += 1
            else:
                curr_overlap -= 1
                j += 1
        
        return max_overlap
        
