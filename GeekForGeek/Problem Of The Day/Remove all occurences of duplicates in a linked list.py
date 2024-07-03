#User function Template for python3

"""
# Linked list Node class

    class Node :
        def __init__(self, val):
            self.data = val
            self.next = None

"""

class Solution:
    def removeAllDuplicates(self, head):
        if not head:
            return None

        dummy = Node(-1)
        dummy.next = head
        prev = dummy
        current = head

        while current:
            is_duplicate = False
            while current.next and current.data == current.next.data:
                current = current.next
                is_duplicate = True
            if is_duplicate:
                prev.next = current.next
            else:
                prev = prev.next
            current = current.next

        return dummy.next
