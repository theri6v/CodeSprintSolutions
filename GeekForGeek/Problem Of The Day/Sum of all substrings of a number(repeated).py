class Solution:
    def sumSubstrings(self,s):
        sub=[]
        n=len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                sub.append(s[i:j])
        count=0
        for i in sub:
            count+=int(i)
        return count  
