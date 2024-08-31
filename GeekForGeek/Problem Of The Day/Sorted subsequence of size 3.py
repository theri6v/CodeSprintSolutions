#User function Template for python3



class Solution:
    def find3Numbers(self, arr):
        # Code Her
            
        n = len(arr)
        if n < 3:
            return []  # Not enough elements to form the required subsequence

    # Initialize arrays for left and right tracking
        min_left = [float('inf')] * n
        min_left_index = [-1] * n
        max_right = [float('-inf')] * n
        max_right_index = [-1] * n

    # Fill min_left and min_left_index
        min_left[0] = arr[0]
        min_left_index[0] = 0
        for i in range(1, n):
            if arr[i] < min_left[i-1]:
                min_left[i] = arr[i]
                min_left_index[i] = i
            else:
                min_left[i] = min_left[i-1]
                min_left_index[i] = min_left_index[i-1]

    # Fill max_right and max_right_index
        max_right[n-1] = arr[n-1]
        max_right_index[n-1] = n-1
        for i in range(n-2, -1, -1):
            if arr[i] > max_right[i+1]:
                max_right[i] = arr[i]
                max_right_index[i] = i
            else:
                max_right[i] = max_right[i+1]
                max_right_index[i] = max_right_index[i+1]

    # Find the subsequence
        for j in range(1, n-1):
            if min_left[j-1] < arr[j] < max_right[j+1]:
                i = min_left_index[j-1]
                k = max_right_index[j+1]
                return [arr[i], arr[j], arr[k]]

        return []

