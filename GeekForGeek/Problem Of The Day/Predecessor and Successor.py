'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
def findPreSuc(self, root, key):
        # code here
        pred, succ = Node(float('-inf')), Node(float('inf'))
        def dfs(n, key):
            nonlocal pred, succ
            if not n:
                return
            
            dfs(n.left, key)
            if n.data < key and n.data > pred.data:
                pred = n 
            if n.data > key and n.data < succ.data:
                succ = n
            dfs(n.right, key)
        dfs(root, key)
        if pred.data == float('-inf'):
            pred.data = -1
        if succ.data == float('inf'):
            succ.data = -1
        return pred, succ
