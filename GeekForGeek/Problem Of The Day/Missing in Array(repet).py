class Solution:
    def missingNum(self, arr):
        arr.sort()
        if(max(arr)==arr[-1] and len(arr)==max(arr)):
            return arr[-1]+1
        else:
            n=max(arr)
            return (n*(n+1)//2)-sum(arr)
