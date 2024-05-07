#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

def reverseLevelOrder(root):
    # This function performs a reverse level order traversal of a binary tree.
    # It returns a list containing the node values in reverse level order. #susovan
    ans=[]
    if root==None:
        return 
    q=deque()
    q.append(root)
    while q:
        n=len(q)
        for i in range(n):
            temp=q.popleft()
            ans.append(temp.data)
            if temp.right:
                q.append(temp.right)
            if temp.left:
                q.append(temp.left)

    ans.reverse()        
    return ans
