#User function Template for python3


class Solution:
    def getMaxArea(self,arr):
        #code here
        n=len(arr)
        s=[]
        maxi=0
        for i in range(n):
            while s and s[-1][0]>arr[i]:
                a,b=s.pop()
                c=-1
                if s:
                    c=s[-1][1]
                ans=a*(i-c-1)
                maxi=max(maxi,ans)
            s.append((arr[i],i))
        while s:
            a,b=s.pop()
            c=-1
            if s:
                c=s[-1][1]
            ans=a*(n-c-1)
            maxi=max(maxi,ans)
        return maxi

    def maxArea(self,M, n, m):
        # code here
        for j in range(m):
            sum=M[0][j]
            for i in range(1,n):
                sum+=M[i][j]
                if M[i][j]==0:
                    sum=0
        
                else:
        
                    M[i][j]=sum
        ans=0
        for i in range(n):
            ans=max(ans,self.getMaxArea(M[i]))
        return ans
                
                



