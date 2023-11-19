#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    
    def solve(self, root, k, su, d):
        if root == None:
            return 
        su += root.data
        self.count += d.get(su-k, 0)
        d[su] = d.get(su, 0) + 1
        self.solve(root.left, k, su, d)
        self.solve(root.right, k, su, d)
        d[su] -= 1
    
    def sumK(self, root, k):
        self.count = 0
        su = 0
        d = {0: 1}
        self.solve(root, k, su, d)
        return self.count
