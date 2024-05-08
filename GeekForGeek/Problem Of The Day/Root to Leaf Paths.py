
from typing import Optional
from collections import deque

from typing import List

"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        # code here
        res = []
        def dfs(node, temp):
            if not node:
                return
            temp.append(node.data)
            if not node.left and not node.right:
                res.append(list(temp))
                temp.pop()
                return
            dfs(node.left, temp)
            dfs(node.right, temp)
            temp.pop()
        dfs(root, [])
        return res
        

