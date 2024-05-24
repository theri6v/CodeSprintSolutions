class Solution:
    #Your task is to complete this function
    #Function should return an integer
    #a - list/array containing height of stack's respectively
    def max_Books(self, n, k, arr):
        #code here
        count = max = 0
        if n == 0: return 0
        for i in range(n):
            if arr[i] <= k:
                count += arr[i]
                max = count if count > max else max
            else: count = 0
        return max
