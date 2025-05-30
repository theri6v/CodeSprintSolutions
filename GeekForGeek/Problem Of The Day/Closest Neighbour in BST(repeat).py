'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        #code here
        res = -1
        
        def dfs(root):
            nonlocal res
            if not root:
                return 
            
            if res!=-1 and res < root.data <= k:
                res = root.data
            elif root.data <= k and res == -1:
                res = root.data
            
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        
        return res
