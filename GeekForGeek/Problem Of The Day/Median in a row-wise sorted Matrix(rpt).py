class Solution:
    def median(self, mat):
        #sam
        arr = []
        for i in mat:
            arr+=i
        arr.sort()
        mid = arr[len(arr)//2]
        return mid
