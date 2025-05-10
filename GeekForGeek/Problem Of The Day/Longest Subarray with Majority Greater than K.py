class Solution:
    def longestSubarray(self, arr, k):

        t = [1 if i > k else -1 for i in arr]
        n = len(t)
        m = 0
        p = 0
        a = {}
        
        for i in range(n):
            p = p + t[i]
            
            if p > 0:
                m = i + 1
                
            else:
                if (p-1) in a:
                    m = max(m,i-a[p-1])
                    
                if p not in a:
                    a[p] = i
                    
        return m
