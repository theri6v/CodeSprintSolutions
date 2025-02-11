#User function Template for python3


class Solution:
    
    def isBST(self, root): 
        min_val = -sys.maxsize - 1  
        max_val = sys.maxsize       
        return self.sol(root, min_val, max_val)
    def sol(self, root, min_val, max_val):
        if root is None:
            return True
        if root.data >= max_val or root.data <= min_val:
            return False
        return self.sol(root.left, min_val, root.data) and self.sol(root.right, root.data, max_val)

