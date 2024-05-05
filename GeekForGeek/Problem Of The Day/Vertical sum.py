#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Complete the function below
    def verticalSum(self, root):
        #:param root: root of the given tree.
        hmap = {}
        self.solve(root, hmap, 0)
        li = sorted([item for item in hmap.items()])
        return [i[1] for i in li]
    
    def solve(self, root, hmap, x):
        if not root: return
        hmap[x] = hmap.get(x, 0) + root.data
        self.solve(root.left, hmap, x-1)
        self.solve(root.right, hmap, x+1)
        return
        
