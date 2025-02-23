class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        # Get the number of nodes in the tree from the length of preorder list.
        node_count = len(preorder)
      
        # If the tree is empty, return None.
        if node_count == 0:
            return None
          
        # The first element from the preorder list is always the root node.
        root = TreeNode(preorder[0])
      
        # If the tree only has one node, return it as the root.
        if node_count == 1:
            return root
      
        # Iterate through the postorder list to find the root of left subtree.
        for i in range(node_count - 1):
            # Preorder[1] would be the root of the left subtree if such exists.
            if postorder[i] == preorder[1]:
                # Using the found index, divide preorder & postorder lists
                # to construct the left subtree.
                root.left = self.constructFromPrePost(
                    preorder[1: 1 + i + 1], postorder[:i + 1]
                )
              
                # The remaining elements in preorder & postorder lists
                # are used to construct the right subtree.
                root.right = self.constructFromPrePost(
                    preorder[1 + i + 1:], postorder[i + 1: -1]
                )
              
                # Return the constructed binary tree root.
                return root
