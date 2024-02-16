#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

import sys
sys.setrecursionlimit(10000)
class Solution:
    def inorder(self,root,prev):
        if root:
            self.inorder(root.left,prev)
            root.left=None
            prev[0].right=root
            prev[0]=root
            self.inorder(root.right,prev)
    def flattenBST(self, root):
        temp=Node(0)
        self.inorder(root,[temp])
        return temp.right

