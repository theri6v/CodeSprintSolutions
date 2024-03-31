#User function Template for python3


'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.key = value
        self.right = None
'''

class Solution:
    def findMaxForN(self, root, n):
        ans=float('-inf')
        
        while root:
            if root.key==n:
                return root.key
            elif root.key>n:
                root=root.left
            else:
                ans=max(ans,root.key)
                root=root.right
                
        return -1 if ans ==float('-inf') else ans
            
