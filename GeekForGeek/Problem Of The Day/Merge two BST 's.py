#User function Template for python3
class Solution:
    
    def inorder(self,root,ans):
        if root is None:
            return
        self.inorder(root.left,ans)
        ans.append(root.data)
        self.inorder(root.right,ans)
    
    def merge(self, root1, root2):
        # code here
        ans=[]
        self.inorder(root1,ans)
        self.inorder(root2,ans)
        ans.sort()
        return ans
