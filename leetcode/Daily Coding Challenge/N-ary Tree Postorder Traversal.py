"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        # Initialize the list to store the postorder traversal result
        postorder_result = []
        
        # Return an empty list if the tree is empty
        if root is None:
            return postorder_result
        
        # Use a stack to perform iterative postorder traversal
        stack = [root]
        
        while stack:
            # Pop a node from the stack
            current_node = stack.pop()
            
            # Append the current node's value to the result list
            postorder_result.append(current_node.val)
            
            # Add all children of the current node to the stack
            # Add children in the order from left to right so they are processed
            # in reverse order when popped from the stack
            for child in current_node.children:
                stack.append(child)
        
        # Reverse the result list to get the correct postorder traversal
        return postorder_result[::-1]
