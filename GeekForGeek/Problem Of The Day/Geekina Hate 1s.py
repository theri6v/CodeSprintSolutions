
from typing import List
from math import factorial,log2


class Solution:
    def findNthNumber(self, n : int, k : int ) -> int:
        # code here
        def combi(n,r):
            return factorial(n)//(factorial(r)*factorial(n-r)) if n>=r else 0
        def countset(x,k):
            if k==0:
                return 1
            if x==0:
                return 0
            h=int(log2(x))
            if h<k-1:
                return 0
            return combi(h,k)+countset(x^(1<<h),k-1)
        def total(x,k):
            return sum(countset(x,i) for i in range(k+1))
        low,high=0,10**15
        while low<high:
            mid=low+(high-low)//2
            if total(mid,k)>=n:
                high=mid
            else:
                low=mid+1
        return low

