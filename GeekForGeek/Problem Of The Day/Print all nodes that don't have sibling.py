#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
def noSibling(root):
    # code here
    res = []
    def inorder(root):
        if root == None:
            return
        inorder(root.left)
        if root.left == None and root.right != None:
            res.append(root.right.data)
        elif root.left != None and root.right == None:
            res.append(root.left.data)
        inorder(root.right)
    inorder(root)
    
    return sorted(res) if len(res) else [-1]
