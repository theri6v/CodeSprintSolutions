class Solution:
    def missingRange(self, arr, low, high):
        new=[]
        s=set(arr)
        for i in range(low,high+1):
            if i not in s:
                new.append(i)
        return new
