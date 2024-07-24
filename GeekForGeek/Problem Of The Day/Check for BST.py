#User function Template for python3

class Solution:
    def __init__(self):
        self.prev=-1
        
    def isBST(self,root):
        if root:
            if not self.isBST(root.left):
                return False
            if root.data<=self.prev:
                return False
            self.prev=root.data
            if not self.isBST(root.right):
                return False
        return True
