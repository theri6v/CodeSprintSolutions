class Solution:
    def countTriplets(self, arr, target):
        n = len(arr)
        count = 0
    
        # Iterate through the array
        for i in range(n - 2):
            left, right = i + 1, n - 1  # Initialize two pointers
    
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                
                if current_sum == target:
                    # Handle duplicates properly
                    if arr[left] == arr[right]:  # All pairs are the same
                        count += (right - left + 1) * (right - left) // 2
                        break
                    else:
                        # Count all pairs between left and right
                        left_val = arr[left]
                        right_val = arr[right]
                        left_count = 0
                        right_count = 0
                        
                        # Count duplicates on the left
                        while left < right and arr[left] == left_val:
                            left += 1
                            left_count += 1
                        
                        # Count duplicates on the right
                        while right >= left and arr[right] == right_val:
                            right -= 1
                            right_count += 1
                        
                        # Add combinations of these duplicates
                        count += left_count * right_count
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
    
        return count
