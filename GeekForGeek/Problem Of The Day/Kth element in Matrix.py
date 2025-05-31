class Solution:
    def kthSmallest(self, matrix, k):
        # code here
        arr = [j for i in matrix for j in i]
        arr.sort()
        return arr[k-1]
