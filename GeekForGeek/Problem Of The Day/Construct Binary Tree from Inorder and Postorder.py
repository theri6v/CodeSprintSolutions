#User function Template for python3

'''
class Node:
            def __init__(self, data):
                self.data = data
                self.left = self.right = None
'''

#Function to return a tree created from postorder and inoreder traversals.
class Solution:
    def buildTree(self, In, post, n):
        # your code here
        if not post:
            return None
        
        root_ele = post[-1]
        root = Node(root_ele)
        idx = In.index(root_ele)
        root.left = self.buildTree(In[:idx], post[:idx], n)
        root.right = self.buildTree(In[idx + 1:], post[idx:-1], n)
        
        return root

