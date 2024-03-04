#User function Template for python3

class Solution:
    def swapElements(self, arr, n):
        #Code here
        for i in range(n-2):
            a=arr[i]
            arr[i]=arr[i+2]
            arr[i+2]=a
        return arr
        
