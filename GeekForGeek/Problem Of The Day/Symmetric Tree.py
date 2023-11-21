#User function Template for python3

class Solution:
    def isSymmetric(self, root):
        # Helper function to check symmetry between two nodes
        def isSymmetricNodes(node1, node2):
            # Base case: Both nodes are None, indicating symmetry
            if not node1 and not node2:
                return True
            # If one node is None and the other is not, it's not symmetric
            elif not node1 or not node2:
                return False
            # If data of the nodes is not equal, it's not symmetric
            elif node1.data != node2.data:
                return False
            # Recursively check symmetry of subtrees
            return isSymmetricNodes(node1.left, node2.right) and isSymmetricNodes(node1.right, node2.left)

        # Check symmetry starting from the left and right subtrees of the root
        return True if not root else isSymmetricNodes(root.left, root.right)
