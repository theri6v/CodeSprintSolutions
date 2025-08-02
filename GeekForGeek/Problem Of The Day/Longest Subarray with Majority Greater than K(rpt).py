class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        # Transform array: 1 if element > k else -1
        trans = [1 if x > k else -1 for x in arr]
        prefix = 0
        # Dictionary to store first occurrence of prefix sums
        first_occurrence = {0: -1}
        max_len = 0

        for i in range(n):
            prefix += trans[i]
            # If prefix sum > 0, subarray (0...i) works
            if prefix > 0:
                max_len = i + 1
            # Check if prefix-1 seen before
            if (prefix - 1) in first_occurrence:
                prev_index = first_occurrence[prefix - 1]
                max_len = max(max_len, i - prev_index)
            # Record first occurrence of prefix sum
            if prefix not in first_occurrence:
                first_occurrence[prefix] = i
        
        return max_len
