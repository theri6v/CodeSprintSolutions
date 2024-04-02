# class Node:
#     def __init__(self):
#         self.data = None
#         self.left = None
#         self.right = None
        
class Solution:
    res = 10000000001
    prev = None
    def absolute_diff(self,root):
        # Your code here
        li = []
        def f(root):
            if root == None:
                return
            
            f(root.left)
            if self.prev != None:
                self.res = min(self.res,root.data - self.prev)
            self.prev = root.data
            f(root.right) 
            
        f(root)
        
        return self.res
