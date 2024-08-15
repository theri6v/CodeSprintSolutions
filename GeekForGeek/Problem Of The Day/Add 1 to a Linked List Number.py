#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def reverse(self,head):
        curr=head
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev
    
    def addOne(self,head):
        head=self.reverse(head)
        curr=head
        prev=None
        while curr and curr.data==9:
            curr.data=0
            prev=curr
            curr=curr.next
        if curr:
            curr.data+=1
        else:
            prev.next=Node(1)
        head=self.reverse(head)
        return head
