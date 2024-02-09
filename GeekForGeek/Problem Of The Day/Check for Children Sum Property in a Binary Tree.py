#User function Template for python3

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isSumProperty(self, root):
        if not root or (not root.left and not root.right):
            return 1
       
        l, r, sum1 = 1, 1, 0
       
        if root.left:
            l = self.isSumProperty(root.left)
            sum1 += root.left.data
        if root.right:
            r = self.isSumProperty(root.right)
            sum1 += root.right.data
       
        return int(root.data == sum1) and l and r

