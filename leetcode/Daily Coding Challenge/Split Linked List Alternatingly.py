#User function Template for python3
'''
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def alternatingSplitList(self, head):
        #Your code here
        h1=head
        h2=head.next
        ptr1=h1
        ptr2=h2
        res=[h1,h2]
        while(ptr2!=None and ptr2.next!=None):
            ptr1.next=ptr2.next
            ptr1=ptr1.next
            ptr2.next=ptr1.next
            ptr2=ptr2.next
        ptr1.next=None
        return res
        
