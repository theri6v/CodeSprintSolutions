class Solution:
    def countTriangles(self, arr):
        from bisect import bisect_left
        arr.sort()
        res=0
        for i in range(len(arr)-1,1,-1):
            for j in range(i-1,0,-1):
                ind=bisect_left(arr,arr[i]-arr[j]+1)
                if ind>=j:
                    break
                else:
                    res+=j-ind
        
        return res
