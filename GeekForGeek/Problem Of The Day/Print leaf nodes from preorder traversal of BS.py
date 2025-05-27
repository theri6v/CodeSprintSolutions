class Solution:
    def leafNodes(self, preorder):
        lth=len(preorder)
        ret=[]
        def dfs(sta=0,sto=lth):
            nonlocal preorder,ret
            if sta+1>sto:
                return
            if sta+1==sto:
                ret.append(preorder[sta])
                return
            ix=sta+1
            while ix<sto and preorder[ix]<preorder[sta]:
                ix+=1
            dfs(sta+1,ix)
            dfs(ix,sto)
        dfs()
        return ret
