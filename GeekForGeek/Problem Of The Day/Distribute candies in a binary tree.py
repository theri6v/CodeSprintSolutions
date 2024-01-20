#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def distributeCandy(self, root):
        def dfs(node=root):
            if not node:
                return 0,0,0
            l=dfs(node.left)
            r=dfs(node.right)
            res=abs(l[0]-l[1]+r[0]-r[1]+node.data-1)
            return l[0]+r[0]+node.data,l[1]+r[1]+1,res+l[2]+r[2]
        return dfs(root.left)[2]+dfs(root.right)[2]
