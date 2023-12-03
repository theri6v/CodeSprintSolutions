#User function Template for python3
class Solution:
    def dfs(self, root, s):
        if root == None: return
        s.add(root.data)
        self.dfs(root.left, s)
        if root.data < x: self.dfs(root.right, s)
    def dfs2(self, root, s, x, ans):
        if root == None: return
        if x - root.data in s:
            ans[0] += 1
        self.dfs2(root.left, s, x, ans)
        if root.data < x: self.dfs2(root.right, s, x, ans)
    def countPairs(self, root1, root2, x): 
        s = set()
        self.dfs(root1, s)
        ans = [0]
        self.dfs2(root2, s, x, ans)
        return ans[0]
