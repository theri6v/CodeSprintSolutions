#User function Template for python3

class Solution:
    def search(self,arr,key):
        # Complete this function
        for i in range(0,len(arr)):
            if arr[i] == key:
                return i
        return -1   

 
