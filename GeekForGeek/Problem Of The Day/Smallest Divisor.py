class Solution:
    def smallestDivisor(self, arr, k):
        def ok(m):
            nonlocal arr,k
            sm=0
            for v in arr:
                sm+=v//m+int(v%m>0)
                if sm>k:
                    return False
            return True
        l=1
        r=max(arr)+1
        while l<r:
            m=l+(r-l)//2
            if ok(m):
                r=m
            else:
                l=m+1
        return l
