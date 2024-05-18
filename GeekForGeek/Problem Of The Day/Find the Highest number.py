#User function Template for python3
from typing import List

class Solution:
    def findPeakElement(self, a):
        low = 0
        high = len(a) - 1
        maxi = -1 # as given array elements are positive
        while low<=high:
            mid = (low+high)//2
            maxi=max(maxi,a[mid])
            if mid == 0:
                low = mid+1
            elif mid == n-1 : 
                high = mid-1
            elif a[mid] < a[mid-1] :#strictly decreasing portion
                high = mid-1
            else: # strictly increasing portion => a[mid] < a[mid+1]
                low = mid+1
        return maxi

