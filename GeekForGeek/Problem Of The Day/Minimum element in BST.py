#User function Template for python3

"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""

        ##Your code here
class Solution:
    #Function to find the minimum element in the given BST.
    def minValue(self, root):
        while root.left:
            root=root.left
        return root.data
