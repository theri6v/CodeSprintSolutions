#User function Template for python3

class Solution:
    def printArr(self, n, arr):
        pass

    def setToZero(self, n, arr):
        # setting all elements to zero
        for i in range(n):
            arr[i] = 0
        print(*arr)
        

    def xor1ToN(self, n, arr):
        nlist = []
        for i in range(1,n+1):
            nlist.append(arr[i-1] ^ (i-1))
        
        print(*nlist)
