class Solution:
    def nodeSum(self, root, l, r):
        found=False
        ret=0
        def dfs(cur=root):
            nonlocal l,r,found,ret
            if not cur:
                return
            dfs(cur.left)
            if l<=cur.data<=r:
                found=True
                ret+=cur.data
            if found and (cur.data<l or cur.data>r):
                return
            dfs(cur.right)
        dfs()
        return ret
