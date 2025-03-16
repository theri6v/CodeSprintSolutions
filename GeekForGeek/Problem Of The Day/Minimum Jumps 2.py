class Solution:
    def minJumps(self, arr):
        # code here
        cur, prv, step = 0, -1, 0
        while cur < len(arr) - 1:
            mx = max([prv+1+i+e for i,e in enumerate(arr[prv+1:cur+1])])
            if mx>cur:
                cur, prv, step = mx, cur, step+1
            else:
                return -1
        return step
