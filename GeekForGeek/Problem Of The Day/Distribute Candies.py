class Solution:
    ans = 0
    
    def solve(self, root):
        if not root: return 0
        left = self.solve(root.left)
        right = self.solve(root.right)
        ttl = left+right+root.data-1
        self.ans += abs(ttl)
        return ttl
    
    def distCandy(self, root):
        self.solve(root)
        return self.ans
