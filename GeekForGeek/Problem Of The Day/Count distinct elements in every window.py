from collections import defaultdict
class Solution:
    def countDistinct(self, arr, k):
        # Code here
        n=len(arr)
        res=[]
        freq=defaultdict(int)
        
        for i in range(k):
            freq[arr[i]]+=1
        res.append(len(freq))
        
        for i in range(k,n):
            freq[arr[i]]+=1
            freq[arr[i-k]]-=1
            
            if freq[arr[i-k]]==0:
                del freq[arr[i-k]]
            res.append(len(freq))
        return res
