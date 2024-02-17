class Solution:
    def isMaxHeap(self, arr, n):
        # Your code goes here
        for item in range(1, n):
            parentNode = (item + 1) // 2
            if arr[parentNode - 1] < arr[item]:
                return False
        return True
