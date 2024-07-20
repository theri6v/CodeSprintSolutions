class Solution:
    def RemoveHalfNodes(self, node):
        if node == None:
            return None
        node.left = self.RemoveHalfNodes(node.left)
        node.right = self.RemoveHalfNodes(node.right)
        if node.left == None and node.right != None:
            return node.right
        if node.left != None and node.right == None:
            return node.left
        return node
