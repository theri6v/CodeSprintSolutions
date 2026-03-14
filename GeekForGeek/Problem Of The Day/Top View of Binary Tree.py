#User function Template for python3

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        q=deque()
        hm=dict()
        q.append([root,0])
        while q:
            cur=q.popleft()
            node=cur[0]
            level=cur[-1]
            if node.left:
                l=level-1
                q.append([node.left,l])
            if node.right:
                l=level+1
                q.append([node.right,l])
            if level not in hm:
                hm[level]=node.data
        s=sorted(hm.items(),key=lambda x:x[0])
        res=[]
        for i in s:
            res.append(i[-1])
        return res
