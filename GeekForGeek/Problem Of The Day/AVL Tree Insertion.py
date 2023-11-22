class Solution:
   def getHeight(self,root):
       if root==None:
           return 0
       return root.height
       
   def getBalance(self,root):
       if root==None:
           return 0
       return self.getHeight(root.left)-self.getHeight(root.right)
       
   def leftRotate(self,root):
       y=root.right
       t2=y.left
       root.right=t2
       y.left=root
       root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))
       y.height=1+max(self.getHeight(y.left),self.getHeight(y.right))
       return y
       
   def rightRotate(self,root):
       y=root.left
       t2=y.right
       root.left=t2
       y.right=root
       root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))
       y.height=1+max(self.getHeight(y.left),self.getHeight(y.right))
       return y
       
       
   def insertToAVL(self, root, key):
       # add key to AVL (if it is not present already)
       # return root node
       if not root:
           root=Node(key)
           return root
       elif key==root.data:
           return root
       elif key<root.data:
           root.left=self.insertToAVL(root.left,key)
       else:
           root.right=self.insertToAVL(root.right,key)
           
           
       root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))
       
       
       b=self.getBalance(root)
       #L-L case
       if b>1 and key<root.left.data:
            return self.rightRotate(root)
       #R-R case
       if b<-1 and key>root.right.data:
           return self.leftRotate(root)
       #L-R case
       if b>1 and key>root.left.data:
           root.left=self.leftRotate(root.left)
           return self.rightRotate(root)
       #R-L case
       if b<-1 and key<root.right.data:
           root.right=self.rightRotate(root.right)
           return self.leftRotate(root)
       return root
