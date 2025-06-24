class Solution:
    def maxSubseq(self, s, k):
        k1=k
        ret=[]
        for c in s:
            while k>0 and ret and ret[-1]<c:
                ret.pop()
                k-=1
            ret.append(c)
        return ''.join(ret[:len(s)-k1])
