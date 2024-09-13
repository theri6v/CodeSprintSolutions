#User function Template for python3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def mirror(self, root):
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.mirror(root.left)
        self.mirror(root.right)
