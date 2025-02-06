#User function Template for python3

'''
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''
# Note: Build tree and return root node

def search(inorder, value, left, right):
    for i in range(left, right + 1):
        if inorder[i] == value:
            return i
    return -1
    
def buildTreeRecur(inorder, preorder, preIndex, left, right):
    # For empty inorder array, return null
    if left > right:
        return None

    rootVal = preorder[preIndex[0]]
    preIndex[0] += 1

    # create the root Node
    root = Node(rootVal)

    # find the index of Root element in the in-order array.
    index = search(inorder, rootVal, left, right)

    # Recursively create the left and right subtree.
    root.left = buildTreeRecur(inorder, preorder, preIndex, left, index - 1)
    root.right = buildTreeRecur(inorder, preorder, preIndex, index + 1, right)

    return root

class Solution:
    def buildTree(self, inorder, preorder):
        # code here
        preIndex = [0]
        return buildTreeRecur(inorder, preorder, preIndex, 0, len(preorder) - 1)
