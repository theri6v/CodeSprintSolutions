class Solution:
    def transitionPoint(self, arr, n): 
        # Code here
        if 1 in arr:
            for i in range(n):
                if arr[i]==1:
                    return i
        else:
            return -1
