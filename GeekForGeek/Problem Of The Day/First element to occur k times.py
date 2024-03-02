#User function Template for python3

class Solution:
    def firstElementKTime(self, n, k, a):
        count_map = {}  # Dictionary to store the count of occurrences for each element
        first_occurrence_index = float('inf')

        for i in range(n):
            if a[i] not in count_map:
                count_map[a[i]] = 1
            else:
                count_map[a[i]] += 1
    
            # Check if the element occurs at least k times
            if count_map[a[i]] == k:
                first_occurrence_index = min(first_occurrence_index, i)
    
        if first_occurrence_index == float('inf'):
            return -1  # No element occurs at least k times
        else:
            return a[first_occurrence_index]
       # code here
    
