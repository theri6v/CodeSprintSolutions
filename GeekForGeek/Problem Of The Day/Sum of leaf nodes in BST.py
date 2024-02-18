#User function Template for python3

##Structure of node
'''
class Node:
    def __init__(self, data=0):
        self.data=0
        self.left=None
        self.right=None
'''

class Solution:
    def sumOfLeafNodes(self, root):
        #Your code here
        if not root:
            return 0
        elif not root.left and not root.right:
            return root.data
        else:
            return self.sumOfLeafNodes(root.left)+self.sumOfLeafNodes(root.right)
