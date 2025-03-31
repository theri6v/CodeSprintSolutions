class Solution:
    def maxPartitions(self , s):
        # code here
        intervals = {ch:i for i,ch in enumerate(s)}
        fmx = -1
        cnt = 0
        
        for i, ch in enumerate(s):
            fmx = max(fmx,intervals[ch])
            if fmx == i:
                cnt += 1
                
        return cnt
