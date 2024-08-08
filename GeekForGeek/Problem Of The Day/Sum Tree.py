#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def is_sum_tree(self, node):
      
        if node is None or (node.left is None and node.right is None):
            return True
        
        left_sum = self.sum_tree(node.left)
        right_sum = self.sum_tree(node.right)
        
        if node.data == left_sum + right_sum:
            return self.is_sum_tree(node.left) and self.is_sum_tree(node.right)
        else:
            return False
    
    def sum_tree(self, node):
        if node is None:
            return 0
        return node.data + self.sum_tree(node.left) + self.sum_tree(node.right)

        # code here
