class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # Define a large number for modulo operation to prevent integer overflow
        mod = 10**9 + 7
      
        # Initialize the count of subarrays with even and odd sum
        count = [1, 0]  # Even sums are initialized to 1 due to the virtual prefix sum of 0 at the start
      
        # Initialize answer and prefix sum variables
        answer = 0
        prefix_sum = 0
      
        # Iterate over the array elements
        for num in arr:
            # Update the prefix sum
            prefix_sum += num
          
            # Increment the answer by the number of subarrays encountered so far
            # that when added to the current element yields an even sum
            answer = (answer + count[prefix_sum % 2 ^ 1]) % mod
          
            # Update the count of subarrays with current sum parity
            count[prefix_sum % 2] += 1
          
        # Return the final answer
        return answer
