from collections import defaultdict
class Solution:
    def totalElements(self, arr):
        dic=defaultdict(int)
        i=0
        j=0
        maxi=0
        while j<len(arr) and i<len(arr):
            dic[arr[j]]+=1
            if len(dic)<=2:
                maxi=max(maxi,j-i+1)
                j+=1
            else:
                dic[arr[i]]-=1
                if dic[arr[i]]==0:
                    del dic[arr[i]]
                i+=1
                j+=1
        maxi=max(maxi,j-i)
        return maxi
