#User function Template for python3

'''
@input - 
node - root node of given tree
k = distance of nodes required 

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    #Function to return count of nodes at a given distance from leaf nodes.
    def printKDistantfromLeaf(self, root, k):
        #code here
        res = set()
        path = []
    
        def dfs(node):
            if not node:
                return
    
            path.append(node)
    
            if not node.left and not node.right:
                if len(path) > k:
                    res.add(path[-(k+1)])
    
            dfs(node.left)
            dfs(node.right)
    
            path.pop()  
    
        dfs(root)
        return len(res)
