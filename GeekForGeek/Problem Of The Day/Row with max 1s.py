#User function Template for python3
class Solution:

    def rowWithMax1s(self,arr):
        # code here
        n = len(arr)
        m = len(arr[0])
        list1=[]
        mx=0
        m1=-1
        for i in range(0,n):
            c=0
            for j in range(0,m):
                if(arr[i][j]==1):
                    c=m-j
                    break;
            if c>mx:
                mx=c
                m1=i
        return m1
