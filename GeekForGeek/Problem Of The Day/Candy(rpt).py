class Solution:
    def minCandy(self, arr):
        lth=len(arr)
        c=[1]*lth
        for ix in range(1,lth):
            if arr[ix]>arr[ix-1] and c[ix]<=c[ix-1]:
                c[ix]=c[ix-1]+1
        for ix in range(lth-2,-1,-1):
            if arr[ix]>arr[ix+1] and c[ix]<=c[ix+1]:
                c[ix]=c[ix+1]+1
        return sum(c)
