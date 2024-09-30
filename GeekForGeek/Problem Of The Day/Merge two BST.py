#User function Template for python3
class Solution:
    def inorder(self,root,res):
        if not root:
            return 
        self.inorder(root.left,res)
        res.append(root.data)
        self.inorder(root.right,res)
        
    def merge(self, root1, root2):
        res1,res2 = [],[]
        self.inorder(root1,res1)
        self.inorder(root2,res2)
        i,j,res = 0,0,[]
        while i < len(res1) and j < len(res2):
            if res1[i] < res2[j]:
                res.append(res1[i])
                i += 1
            else:
                res.append(res2[j])
                j += 1
        
        while i < len(res1):
            res.append(res1[i])
            i += 1
        
        while j < len(res2):
            res.append(res2[j])
            j += 1
            
        return res
        
        
