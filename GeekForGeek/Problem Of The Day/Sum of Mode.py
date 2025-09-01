from heapq import heappop,heappush
from collections import defaultdict
class Solution:
    def sumOfModes(self, arr, k):
        # code here
        d=defaultdict(int)
        i=0
        h=[]
        n=len(arr)
        ans=0
        for j in range(n):
            d[arr[j]]+=1
            if j>=k:
                d[arr[j-k]]-=1
            heappush(h,(-d[arr[j]],arr[j]))
            
            while d[h[0][1]]!=-h[0][0]:
                heappop(h)
            if j>=k-1:
                ans+=h[0][1]
        return ans
