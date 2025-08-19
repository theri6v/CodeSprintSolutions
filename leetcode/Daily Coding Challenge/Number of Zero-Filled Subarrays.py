class Solution:
    def zeroFilledSubarray(self, a: List[int]) -> int:
        return sum(accumulate(a,lambda q,v:v==0 and q+1,initial=0))
