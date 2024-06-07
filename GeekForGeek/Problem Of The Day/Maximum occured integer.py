#User function Template for python3

class Solution:
    #Complete this function
    #Function to find the maximum occurred integer in all ranges.
    def maxOccured(self,n, l, r, maxx):
        psum=[0]*(maxx+2)
        for i,j in zip(l,r):
            psum[i]+=1
            psum[j+1]-=1
        for i in range(1,len(psum)):
            psum[i]+=psum[i-1]
        mx=1
        occurence=0
        for i in range(1,maxx+1):
            if occurence<psum[i]:
                mx=i
                occurence=psum[i]
        return mx
