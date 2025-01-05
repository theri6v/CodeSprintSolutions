#User function Template for python3
class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        arr.sort()
        n=len(arr)
        c=0
        l,r=0,n-1
        while l<r:
            if arr[l]+arr[r]<target:
                c+=r-l
                l+=1
            else:
                r-=1
        return c
