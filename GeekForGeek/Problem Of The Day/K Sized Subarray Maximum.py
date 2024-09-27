#User function Template for python3
from collections import deque
class Solution:
    
    def max_of_subarrays(self,k,arr):
        res = []
        max_elem = 0
        dq = deque()
        for i in range(k):
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()
            dq.append(i)
        res.append(arr[dq[0]])
        for i in range(k, len(arr)):
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()
            dq.append(i)
            res.append(arr[dq[0]])
            
        return res
