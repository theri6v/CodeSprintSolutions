class Solution:
    def countSubarrays(self, arr, k):
        # Hash map to store prefix sums and their frequencies
        prefix_sum_map = {0: 1}  # Initialize with 0 sum having frequency 1
        count = 0
        current_sum = 0
        
        for num in arr:
            # Update the current running sum
            current_sum += num
            
            # Check if (current_sum - k) exists in the map
            if (current_sum - k) in prefix_sum_map:
                count += prefix_sum_map[current_sum - k]
            
            # Update the hash map with the current sum
            prefix_sum_map[current_sum] = prefix_sum_map.get(current_sum, 0) + 1
        
        return count
