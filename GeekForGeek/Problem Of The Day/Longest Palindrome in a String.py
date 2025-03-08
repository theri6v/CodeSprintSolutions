
class Solution:
 def longestPalindrome(self, s):
    start,maxLen=0,1
    n=len(s)
    for i in range(n):
        for h in (i,i+1):
            l=i-1
            while l>=0 and h<n and s[l]==s[h]:
                if h-l+1>maxLen:
                    start=l
                    maxLen=h-l+1
                l-=1
                h+=1
    return s[start:start+maxLen]
