from collections import Counter
from heapq import *
class Solution:
    def minValue(self, s, k):
        dic=Counter(s)
        s1=0
        if k==len(s):
            return 0
        heap=[]
        for i,j in dic.items():
            heappush(heap,[-j,i])
        while heap and k:
            a=heappop(heap)
            k-=1
            a[0]+=1
            heappush(heap,a)
        while heap:
            a=heappop(heap)
            s1+=a[0]**2
        return s1
