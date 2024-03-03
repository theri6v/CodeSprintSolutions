#User function Template for python3
class Solution:

    def printLargest(self, n, arr):
        # code here
        return "".join(sorted(arr, reverse=True, key= lambda x:x*13))
