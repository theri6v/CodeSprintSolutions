#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        rep=-1
        for i in range(len(arr)):
            while(arr[i]!=i+1):
                u=arr[i]
                if(arr[u-1]==arr[i]):
                    rep=arr[i]
                    break
                arr[u-1],arr[i]=arr[i],arr[u-1]
        n=len(arr)
        b=rep-sum(arr)+n*(n+1)//2
        return [rep,b]
