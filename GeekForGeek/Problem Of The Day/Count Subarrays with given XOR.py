class Solution:
    def subarrayXor(self, arr, k):
        freq={0:1}
        preXor=0
        ans=0
        for item in arr:
            preXor^=item
            ans+=freq.get(preXor^k,0)
            freq[preXor]=freq.get(preXor,0)+1
            
        return ans
