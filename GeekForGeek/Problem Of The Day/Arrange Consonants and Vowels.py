#User function Template for python3

"""
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    #Function to reverse a linked list.
    vowels={"a","e","i","o","u"}

    def arrangeCV(self, head):
        curr=head
        vHead,p=None,None
        cHead,q=None,None
        while curr:
            if curr.data in self.vowels:
                if vHead:
                    vHead.next=curr
                    vHead=vHead.next
                else:
                    vHead=curr
                    p=curr
                
            else:
                if cHead:
                    cHead.next=curr
                    cHead=cHead.next
                else:
                    cHead=curr
                    q=curr
            curr=curr.next
        if cHead:
            cHead.next=None
        if vHead:
            vHead.next=q
        return p if p else q

