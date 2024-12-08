class Solution:
    def mergeOverlap(self, arr):
        #Code here
    # Step 1: Sort intervals based on the start time
        arr.sort(key=lambda x: x[0])
    
        # Step 2: Use a pointer to keep track of the position in the result
        index = 0  # This serves as the position in the merged intervals
    
        for i in range(1, len(arr)):
            # If the current interval overlaps with the last interval in the merged array
            if arr[index][1] >= arr[i][0]:
                # Merge the two intervals by updating the end time
                arr[index][1] = max(arr[index][1], arr[i][1])
            else:
                # Otherwise, move to the next interval
                index += 1
                arr[index] = arr[i]
    
        # Return the merged intervals up to the index
        return arr[:index + 1]
