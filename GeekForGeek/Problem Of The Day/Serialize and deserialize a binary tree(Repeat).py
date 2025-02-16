#User function Template for python3


'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        
        def inorder(root , res):
            if root:
            
                inorder(root.left , res)
                res.append(root.data)
                inorder(root.right ,res)
        res = []
        inorder(root ,res)
        
        return res
        #code here
    
    #Function to deserialize a list and construct the tree.   
    def deSerialize(self, a):
        
        
        def helper(a, l , r):
            if l > r:
                return 
            idx = (l+r)//2
            
            root = Node(a[idx])
            
            root.left = helper(a , l , idx-1)
            root.right = helper(a, idx +1 , r)
            return root 
        return helper(a, 0 , len(a)-1)
        #code here
 


