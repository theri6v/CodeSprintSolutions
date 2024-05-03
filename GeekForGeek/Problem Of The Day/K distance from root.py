#User function Template for python3



'''
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def KDistance(self,root,k):
        
        que = deque([(root, 0)])
        res = []
        while que:
            node, dist = que.popleft()
            if dist == k:
                res.append(node.data)
            
            else:
                if node.left:
                    que.append((node.left, dist+1))
                if node.right:
                    que.append((node.right, dist+1))
        return res
        
        
        
    '''
    :param root: root of given tree.
    :param k: distance k from root
    :return: list of all nodes that are at distance k from root.
    '''
