#User function Template for python3

class Solution:
    def pushZerosToEnd(self,arr):
        # code here
        res=[]
        zero=[]
        for i in range(len(arr)):
            if arr[i]!=0:
                res.append(arr[i])
            else:
                 zero.append(arr[i])
        arr.clear()
        arr.extend(res)
        arr.extend(zero)
        return arr
