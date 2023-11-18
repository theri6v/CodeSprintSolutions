class Solution:
    def reverseDLL(self, head):
        #return head after reversing
        if head is None or head.next is None:
            return head
        temp=None
        curr=head
        forward=head
        while forward:
            forward=curr.next
            curr.next=temp
            curr.prev=forward
            temp=curr
            curr=forward
        return temp
