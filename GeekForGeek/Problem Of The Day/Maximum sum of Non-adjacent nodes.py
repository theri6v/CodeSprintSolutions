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
    # Function to return the maximum sum of non-adjacent nodes.
    def getMaxSum(self, root):
        
        # Helper function to return a tuple (include, exclude)
        def solve(node):
            if not node:
                return (0, 0)  # (include, exclude)
            
            # Recursively solve for left and right subtrees
            left_incl, left_excl = solve(node.left)
            right_incl, right_excl = solve(node.right)
            
            # If we include current node, we cannot include its children
            incl = node.data + left_excl + right_excl
            
            # If we exclude current node, we can choose to include or exclude its children
            excl = max(left_incl, left_excl) + max(right_incl, right_excl)
            
            return (incl, excl)
        
        # Final result
        incl, excl = solve(root)
        return max(incl, excl)
