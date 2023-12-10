#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        found = {0: 1}
        sum_val = 0

        for i in range(n):
            sum_val += arr[i]

            if sum_val in found:
                return True

            if sum_val not in found:
                found[sum_val] = 1

        return False
  
