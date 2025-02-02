"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""
class Solution:
    def levelOrder(self, root):
        # Your code here
        if root is None:
            return []
            
        q=deque()
        res=[]
        q.append(root)
        curlvl=0
        while q:
            lenq=len(q)
            res.append([])
            for _ in range(lenq):
                node=q.popleft()
                res[curlvl].append(node.data)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            curlvl+=1
        return res
