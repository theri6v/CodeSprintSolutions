#User function Template for python3

class Solution:
    def nextPermutation(self, arr):
         # code here
        idx=-1
        for i in range(len(arr)-2,-1,-1):
            if arr[i]<arr[i+1]:
                idx=i
                break
        if idx==-1:
            return arr.reverse()
        for i in range(len(arr)-1,idx,-1):
            if arr[i]>arr[idx]:
                arr[idx],arr[i]=arr[i],arr[idx]
                break
                
        arr[idx+1:] = arr[idx+1:][::-1]
        return arr
