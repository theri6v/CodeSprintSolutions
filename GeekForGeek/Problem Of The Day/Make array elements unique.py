#User function Template for python3

class Solution:
    def minIncrements(self, arr):
        if not arr:
            return 0

        arr.sort()
        ans = 0

        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                ans += arr[i - 1] - arr[i] + 1
                arr[i] = arr[i - 1] + 1

        return ans
