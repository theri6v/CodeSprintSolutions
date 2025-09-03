class Solution:
    def reverse(self, head):
        # code here
        curr= head
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr.prev=temp
            curr=curr.prev
        return prev
