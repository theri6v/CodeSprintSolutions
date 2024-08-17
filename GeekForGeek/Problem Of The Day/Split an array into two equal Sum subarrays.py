class Solution:
    def canSplit(self, arr):
        #code here
        total = sum(arr)
        if total%2==1:
            return False
        n = len(arr)
        half = 0
        for i in range(n):
            half+=arr[i]
            if half==total//2:
                return True
        return False
