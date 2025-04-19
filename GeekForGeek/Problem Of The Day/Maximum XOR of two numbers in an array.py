#User function Template for python3

class Node:
    def __init__(self):
        self.children=[None]*2

class Solution:
    def insert(self,root,num):
        for i in range(31,-1,-1):
            bit=(num>>i)&1
            if root.children[bit]==None:
                root.children[bit]=Node()
            root=root.children[bit]
    
    def maxXor(self, arr):
        root=Node()
        for item in arr:
            self.insert(root,item)
        ans=0
        for num in arr:
            node=root
            curr=0
            for i in range(31,-1,-1):
                bit=(num>>i)&1
                opposite=1-bit
                if node.children[opposite]:
                    curr=curr<<1|1
                    node=node.children[opposite]
                else:
                    curr=curr<<1|0
                    node=node.children[bit]
            ans=max(ans,curr)
        return ans
