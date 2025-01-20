#User function Template for python3
'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self,head1, head2):
        # code here
        c1 = head1
        c2 = head2
        res = Node(-1)
        r = res
        while c1 != None and c2 != None:
            
            if c1.data < c2.data:
                res.next = c1
                res = res.next
                c1 = c1.next
            else:
                res.next = c2
                res = res.next
                c2 = c2.next
        if c1 is None:
            res.next = c2
        if c2 is None:
            res.next = c1
        
        return r.next
