class Solution:
    def missingNumber(self, arr):
        n = len(arr)
        for i in range(n):
            if 1<=arr[i] <= n:
                temp = arr[arr[i]-1]
                arr[arr[i]-1] = arr[i]
                arr[i] = temp
        
        for i in range(n):
            if 1<=arr[i] <= n:
                temp = arr[arr[i]-1]
                arr[arr[i]-1] = arr[i]
                arr[i] = temp
                
        
        for i in range(n):
            if i+1!=arr[i]:
                return i+1
        return i+2        

