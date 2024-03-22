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
    def diagonalSum(self, root):
        diagonal_sums = {}

        def dfs(node, diagonal_level):
            if not node:
                return
            
            diagonal_sums[diagonal_level] = diagonal_sums.get(diagonal_level, 0) + node.data
            
            dfs(node.left, diagonal_level + 1)
            dfs(node.right, diagonal_level)
    
        dfs(root, 0)
        return diagonal_sums.values()
    
    
    
