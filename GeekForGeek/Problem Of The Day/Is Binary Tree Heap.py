from collections import deque

class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def isComplete(self, root, index, total_nodes):
        if not root:
            return True
        if index >= total_nodes:
            return False
        return (self.isComplete(root.left, 2 * index + 1, total_nodes) and
                self.isComplete(root.right, 2 * index + 2, total_nodes))

    def isMaxHeap(self, root):
        if not root:
            return True
        if root.left:
            if root.data < root.left.data:
                return False
        if root.right:
            if root.data < root.right.data:
                return False
        return self.isMaxHeap(root.left) and self.isMaxHeap(root.right)

    def isHeap(self, root):
        total_nodes = self.countNodes(root)
        return self.isComplete(root, 0, total_nodes) and self.isMaxHeap(root)
