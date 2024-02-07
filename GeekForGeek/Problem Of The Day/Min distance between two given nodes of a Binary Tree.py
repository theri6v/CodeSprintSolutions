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
    def findDist(self, root, a, b):
        def findLCA(node, a, b):
            if not node:
                return None
            if node.data == a or node.data == b:
                return node
            left = findLCA(node.left, a, b)
            right = findLCA(node.right, a, b)
            if left and right:
                return node
            return left if left else right

        def distanceFromLCA(node, val, dist):
            if not node:
                return -1
            if node.data == val:
                return dist
            leftDist = distanceFromLCA(node.left, val, dist + 1)
            if leftDist != -1:
                return leftDist
            return distanceFromLCA(node.right, val, dist + 1)

        lca = findLCA(root, a, b)
        distA = distanceFromLCA(lca, a, 0)
        distB = distanceFromLCA(lca, b, 0)
        return distA + distB
