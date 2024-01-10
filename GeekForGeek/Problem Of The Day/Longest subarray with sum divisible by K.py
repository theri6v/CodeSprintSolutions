#User function Template for python3

class Solution:
    def longSubarrWthSumDivByK (self,arr,  n, K) : 
# Create a hashmap to store the remainder frequencies
        prefix_sum_remainders = {0: -1}  # Handle the case when prefix sum % K == 0
        max_length = 0
        curr_sum = 0
 
        for i in range(n):
            curr_sum += arr[i]
            remainder = curr_sum % K
 
            if remainder in prefix_sum_remainders:
                max_length = max(max_length, i - prefix_sum_remainders[remainder])
            else:
                prefix_sum_remainders[remainder] = i
 
        return max_length

