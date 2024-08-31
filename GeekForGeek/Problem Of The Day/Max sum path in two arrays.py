#Your task is to complete this function
#Function should return an integer denoting the required answer
class Solution:
    def maxPathSum(self, arr1, arr2):
        # Initialize pointers, sums, and result
        i, j = 0, 0
        sum1, sum2 = 0, 0
        result = 0
        n, m = len(arr1), len(arr2)

        # Traverse both arrays using two pointers
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]  # Add elements to sum1 from arr1
                i += 1
            elif arr1[i] > arr2[j]:
                sum2 += arr2[j]  # Add elements to sum2 from arr2
                j += 1
            else:
                # Add the maximum of sum1 and sum2, and the common element once
                result += max(sum1, sum2) + arr1[i]
                # Reset sums
                sum1, sum2 = 0, 0
                # Move past the common element
                i += 1
                j += 1

        # Add remaining elements of arr1 to sum1
        while i < n:
            sum1 += arr1[i]
            i += 1

        # Add remaining elements of arr2 to sum2
        while j < m:
            sum2 += arr2[j]
            j += 1

        # Add the maximum of the remaining sums to the result
        result += max(sum1, sum2)
        
        return result
