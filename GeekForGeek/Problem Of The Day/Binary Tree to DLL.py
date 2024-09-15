#User function Template for python3

'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''
class Solution:
    def inorder(self, root, nodes):
        if not root:
            return
        self.inorder(root.left, nodes)
        nodes.append(root)
        self.inorder(root.right, nodes)

    def bToDLL(self, root):
        nodes = []
        self.inorder(root, nodes)
        
        if len(nodes) == 1:
            return root
        
        for i in range(len(nodes)):
            if i == 0:
                nodes[i].left = None
                nodes[i].right = nodes[i + 1]
            elif i == len(nodes) - 1:
                nodes[i].right = None
                nodes[i].left = nodes[i - 1]
            else:
                nodes[i].left = nodes[i - 1]
                nodes[i].right = nodes[i + 1]
        
        return nodes[0]
