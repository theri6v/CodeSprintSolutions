#User function Template for python3
class Solution:
    def insertionSort(self, head):
        if not head: return head
        res = Node(-1)
        res.next = head
        while(head.next):
            if head.next.data<head.data:
                cur = head.next
                head.next=head.next.next
                ptr = res.next
                prev = res
                while(ptr.data<cur.data):
                    prev = ptr
                    ptr = ptr.next
                prev.next = cur
                cur.next = ptr
                continue
            head=head.next
                
        return res.next
