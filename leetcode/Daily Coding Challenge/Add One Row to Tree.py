# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            return TreeNode(v, left=root)
        self.addOneRowHelper(root, v, d, 1)
        return root
        
        
    def addOneRowHelper(self, root, v, d, level):    
        if d-1 == level:
            leftTree = TreeNode(v, left=root.left)
            rightTree = TreeNode(v, right=root.right)
            
            root.left = leftTree
            root.right = rightTree
            return
        
        if root.left:
            self.addOneRowHelper(root.left, v, d, level+1)
        if root.right:
            self.addOneRowHelper(root.right, v, d, level+1)
