class Solution:
    def countXInRange(self, arr, queries):
        res=[]
        for l,r,x in queries:
            lb = bisect.bisect_left(arr, x, lo=l, hi=r+1)
            ub = bisect.bisect_right(arr, x, lo=l, hi=r+1)
            res.append(ub-lb)
        return res
