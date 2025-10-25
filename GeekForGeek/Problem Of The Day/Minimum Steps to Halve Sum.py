from heapq import *
class Solution:
  def minOperations(self, arr):
    heap=[]
    c=0
    s=sum(arr)
    target=s/2
    for i in arr:
        heappush(heap,-i)
    
    while heap:
        if s<=target:
            return c
        a=-heappop(heap)/2
        s-=a
        c+=1
        heappush(heap,-a)
    return 0
