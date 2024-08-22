#User function Template for python3


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def solve(root,h,li,maxi):
    if root == None:
        return
    if maxi[0] < h:
        maxi[0]=h
        li.append(root.data)
    solve(root.left,h+1,li,maxi)
    solve(root.right,h+1,li,maxi)
#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    
    # code here
    if root == None:
        return
    li=[]
    maxi=[-1]
    solve(root,0,li,maxi)
    return li
