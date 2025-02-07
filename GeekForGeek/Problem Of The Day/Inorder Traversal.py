'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrder(self,root):
        # code here
        res = []
        if root is None:
            return []
        res.extend(self.inOrder(root.left))
        res.append(root.data)
        res.extend(self.inOrder(root.right))
        
        return res
        
