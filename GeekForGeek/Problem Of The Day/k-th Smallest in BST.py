#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    # Return the kth smallest element in the given BST 
    def kthSmallest(self, root, k): 
        #code here.
        def in_order(node):
            if not node:
                return
            yield from in_order(node.left)
            
            yield node.data
            
            yield from in_order(node.right)
        
        count = 0
        for val in in_order(root):
            count += 1
            if count == k:
                return val
        
        return -1
