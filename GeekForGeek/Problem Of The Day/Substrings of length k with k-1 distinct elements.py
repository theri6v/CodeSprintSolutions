from collections import defaultdict
class Solution:
    def substrCount(self, s, k):
        dic=defaultdict(int)
        c=0
        i=0
        j=0
        while j<len(s) and i<=j:
            dic[s[j]]+=1
            if j-i+1==k:
                if len(dic)==k-1:
                    c+=1
                else:
                    dic[s[i]]-=1
                    if dic[s[i]]==0:
                        del dic[s[i]]
                    i+=1
                j+=1
            elif j-i+1<k:
                j+=1
            elif j-i+1>k:
                dic[s[i]]-=1
                if dic[s[i]]==0:
                    del dic[s[i]]
                i+=1
                if len(dic)==k-1 and j-i+1==k:
                    c+=1
                
                j+=1
            
        return c
