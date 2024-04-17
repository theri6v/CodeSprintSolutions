#User function Template for python3
from bisect import bisect_left
class Solution:    
    def countPairs(self,arr, n): 
         # Your code goes here
         for i in range(n):
             arr[i] = i * arr[i]
         s = []
         ans = 0
         for i in range(n - 1, -1, -1):
             if i!=n-1:
                 ans+=bisect_left(s,arr[i])
             s.insert(bisect_left(s,arr[i]),arr[i])
         return ans
