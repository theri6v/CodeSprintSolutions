#User function Template for python3
from collections import defaultdict

class Solution:
    def findSubString(self, str):
        # code here
        n,N=len(str),len(set(str))
        ans,curr,count=n,-1,0
        d=defaultdict(int)
        for i in range(n):
            while curr<(n-1) and count<N:
                curr+=1
                d[str[curr]]+=1
                if d[str[curr]]==1:
                    count+=1
            if count==N:
                ans=min(ans,curr-i+1)
            else:
                break
            d[str[i]]-=1
            if d[str[i]]==0:
                count-=1
        return ans
