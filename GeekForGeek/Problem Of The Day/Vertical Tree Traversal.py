'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def verticalOrder(self, root): 
        # code here
        if not root:
            return []
        
        mp = defaultdict(list)
        q = deque([(root, 0)])
        
        while q:
            node, col = q.popleft()
            mp[col].append(node.data)
            
            if node.left:
                q.append((node.left, col - 1))
            
            if node.right:
                q.append((node.right, col + 1))
        
        return [mp[key] for key in sorted(mp)]
