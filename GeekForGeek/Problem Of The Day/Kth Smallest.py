#User function Template for python3


class Solution:

    def kthSmallest(self, arr,k):
        mine = min(arr)
        maxe = max(arr)
        rs = maxe - mine + 1
        
        freq = [0] * rs
        
        for num in arr:
            freq[num - mine] += 1
        
        c = 0
        for i in range(rs):
            c += freq[i]
            if c >= k:
                return i + mine
        
        return -1
        
        

