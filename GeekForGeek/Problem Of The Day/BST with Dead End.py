class Solution:
    def f(self, root, minVal, maxVal):
        if not root:
            return False
        
        if minVal == maxVal:
            return True
        
        # Check left and right subtrees with updated ranges
        left = self.f(root.left, minVal, root.data - 1)
        right = self.f(root.right, root.data + 1, maxVal)
        
        return left or right

    def isDeadEnd(self, root):
        return self.f(root, 1, 100000)
