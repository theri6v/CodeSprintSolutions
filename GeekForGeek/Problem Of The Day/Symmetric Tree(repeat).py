'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def isSymmetric(self, root):
        def helper(root1,root2):
            if not root1 and not root2:
                return True
            if (not root1 or not root2) or root1.data!=root2.data:
                return False
            return helper(root1.left,root2.right) and helper(root1.right,root2.left)
        return helper(root.left,root.right)
