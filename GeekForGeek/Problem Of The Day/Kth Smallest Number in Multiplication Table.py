class Solution(object):
    def kthSmallest(self, m, n, k):
        #code here
        l=1
        h=m*n
        while l<h:
            mid=l+(h-l)//2
            c=0
            for i in range(1,m+1):
                c+=min(mid//i,n)
            if c<k:
                l=mid+1
            else:
                h=mid
        return l
