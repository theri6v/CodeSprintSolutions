class Solution:
    def rearrange(self, arr):
        n = len(arr)
        result = [-1] * n
        for i in range(n):
            if 0 <= arr[i] < n:
                result[arr[i]] = arr[i]
        return result
