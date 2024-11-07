#User function Template for python3
class Solution:
    def findSplit(self, arr):
        total_sum = sum(arr)
        
        # If total sum is not divisible by 3, we can't split into three equal parts
        if total_sum % 3 != 0:
            return [-1, -1]
        
        target_sum = total_sum // 3
        n = len(arr)
        
        # Variables to track the indices for split points
        first_split = -1
        second_split = -1
        running_sum = 0
        
        # Traverse the array to find the split points
        for i in range(n):
            running_sum += arr[i]
            
            # Check if we have found the first target sum segment
            if running_sum == target_sum and first_split == -1:
                first_split = i
                running_sum = 0  # Reset running sum for the next part
                
            # Check if we have found the second target sum segment after the first
            elif running_sum == target_sum and first_split != -1:
                second_split = i
                # We found both split points, so we can stop here
                break
        
        # If we found two valid split points, return them
        if first_split != -1 and second_split != -1:
            return [first_split, second_split]
        
        # Otherwise, return [-1, -1] indicating it's not possible
        return [-1, -1]

