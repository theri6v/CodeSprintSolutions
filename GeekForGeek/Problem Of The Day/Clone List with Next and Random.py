# Link list Node
# class Node:

#     def __init__(self, x):
#         self.data = x
#         self.next = None
#         self.random = None
        
class Solution:
    def cloneLinkedList(self, head):
        # code here
        if not head: return None
        current = head
        while current:
            copy = Node(current.data)
            copy.next = current.next
            current.next = copy
            current = copy.next
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        original = head
        copyHead = head.next
        copy = copyHead
        while original:
            original.next = original.next.next
            if copy.next:
                copy.next = copy.next.next
            original = original.next
            copy = copy.next
        return copyHead
