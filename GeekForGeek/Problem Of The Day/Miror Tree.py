#User function Template for python3
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    # Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        if root is None:
            return
        
        # Recursively call mirror on left and right subtrees
        self.mirror(root.left)
        self.mirror(root.right)
        
        # Swap the left and right children
        root.left, root.right = root.right, root.left
