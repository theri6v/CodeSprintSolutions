
from typing import List


class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        # code here
        l,h=0,n-1
        while l<=h:
            mid=(l+h)//2
            if k<arr[mid]:
                if mid==0 or arr[mid]-k<=k-arr[mid-1]:
                    return arr[mid]
                else:
                    h=mid-1
            else:
                if mid==n-1 or k-arr[mid]<arr[mid+1]-k:
                    return arr[mid]
                else:
                    l=mid+1




#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        k = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.findClosest(n, k, arr)
        
        print(res)
        

# } Driver Code Ends