#User function Template for python3


'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxSum(self, root): 
        self.max_sum = float('-inf')  # Global variable to store max sum

        def dfs(node):
            if not node:
                return 0  # Base case: Null node contributes 0
            
            # Recursively compute left and right max sum
            left_sum = max(dfs(node.left), 0)  # Ignore negative sums
            right_sum = max(dfs(node.right), 0)  # Ignore negative sums
            
            # Compute max path sum including current node
            current_sum = node.data + left_sum + right_sum
            
            # Update the global max sum
            self.max_sum = max(self.max_sum, current_sum)
            
            # Return the maximum path sum extending from the current node
            return node.data + max(left_sum, right_sum)
        
        dfs(root)  # Start DFS from the root
        return self.max_sum
