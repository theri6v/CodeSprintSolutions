#User function Template for python3

class Solution:
    def kthElement(self, k, arr1, arr2):
        a=arr1+arr2
        a.sort()
        
        return a[k-1]
