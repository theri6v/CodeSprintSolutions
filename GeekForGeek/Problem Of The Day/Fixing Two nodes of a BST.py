'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Fix:
    def __init__(self):
        self.first=None
        self.second=None
        self.pred=Node(0)
class Solution:
    
    # your code here

    def solve(self,root,f):
        if root:
            self.solve(root.left,f)
            if root.data<f.pred.data:
                if not f.second:
                    f.second=f.pred
                f.first=root
            f.pred=root
            self.solve(root.right,f)
    
    def correctBST(self, root):
        f=Fix()
        self.solve(root,f)
        f.first.data,f.second.data=f.second.data,f.first.data

