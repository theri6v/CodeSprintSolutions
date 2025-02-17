class Solution:
    def kLargest(self, arr, k):
        # Your code here
        l=[]
        arr.sort(reverse=True)
        for i in range(k):
            l.append(arr[i])
        return l
