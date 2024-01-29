class Solution:
    def TotalCount(self, s):
        pfs=[int(x) for x in s]
        for i,v in enumerate(pfs):
            if i>=1:
                pfs[i]+=pfs[i-1]
        m=len(pfs)
        from functools import lru_cache
        @lru_cache(None)
        def dp(cur=0,sm=0):
            nonlocal pfs,m
            ans=0
            prv=pfs[cur-1] if cur-1>=0 else 0
            for nxt in range(cur,m):
                left=pfs[nxt]-prv
                right=pfs[m-1]-pfs[nxt]
                if sm<=left<=right:
                    ans+=1+dp(nxt+1,left)
            return ans
        return dp()+1
