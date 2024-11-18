#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        N = len(arr)
        k=d%N
        p=arr[k:]+arr[:k]
        for i in range(len(arr)):
            arr[i]=p[i]
