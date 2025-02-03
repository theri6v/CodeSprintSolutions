#User function Template for python3

# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        if root is None:
            return -1
        l=self.height(root.left)
        r=self.height(root.right)
        return 1+max(l,r)
