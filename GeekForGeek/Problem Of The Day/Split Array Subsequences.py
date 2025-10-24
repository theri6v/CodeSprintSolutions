class Solution:

    def isPossible(self, arr, k):
        # Code here
        l = []
        
        for num in arr:
            flag=1
            for subs in l[::-1]:
                if subs[-1]==num-1:
                    subs.extend([num])
                    flag=0
                    break
            if(flag):        
             l.append([num])
            
        min_size = float('inf')
        for subs in l:
            min_size = min(min_size,len(subs))
            
        if min_size>=k:
            return True
            
        return False
