"""  
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def count(self, head, key):
        # Code here
        c=0
        while(head):
            if(head.data==key):
                c+=1
            head=head.next
        return c
