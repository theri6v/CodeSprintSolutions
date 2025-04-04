# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Helper function to perform a depth-first search on the tree.
        def dfs(node):
            # Base case: if the current node is None, it corresponds to a depth of 0.
            if node is None:
                return None, 0

            # Recursively find the lowest common ancestor and depth of the left subtree.
            left_lca, left_depth = dfs(node.left)
            # Recursively find the lowest common ancestor and depth of the right subtree.
            right_lca, right_depth = dfs(node.right)

            # If the left subtree is deeper, return the left LCA and its depth increased by one.
            if left_depth > right_depth:
                return left_lca, left_depth + 1
            # If the right subtree is deeper, return the right LCA and its depth increased by one.
            if left_depth < right_depth:
                return right_lca, right_depth + 1

            # If both subtrees have the same depth, then this node is the lowest common ancestor.
            # Return the current node and the depth of the subtree.
            return node, left_depth + 1

        # Call the DFS helper function and return the lowest common ancestor.
        return dfs(root)[0]
