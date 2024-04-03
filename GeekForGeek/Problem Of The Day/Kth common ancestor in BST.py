#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def kthCommonAncestor(self, root, k, x, y):
        # Code here
        from collections import deque
        freq={}
        xca=deque()
        yca=deque()
        def kthCA(root,x,ll):
            if root is None:
                return False
            
            if root.data == x:
                ll.append(root.data)
                if root.data in freq:
                    freq[root.data]+=1
                else:
                    freq[root.data]=1
                return True
            
            if kthCA(root.left,x,ll) or kthCA(root.right,x,ll):
                ll.append(root.data)
                if root.data in freq:
                    freq[root.data]+=1
                else:
                    freq[root.data]=1
                return True
            
            return False
        
        kthCA(root,x,xca)
        kthCA(root,y,yca)
        #print(freq,xca,yca)
        i=0
        if len(freq)>=k:
            for val in xca:
                if freq[val] ==2:
                    i+=1
                if i == k:
                    return val
                
        return -1

