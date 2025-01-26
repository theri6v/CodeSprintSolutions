'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    def removeLoop(self, head):
        if not head or not head.next:
            return

        # Step 1: Detect the loop using Floyd's cycle detection algorithm
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # Loop detected
            if slow == fast:
                break
        else:
            # No loop detected
            return

        # Step 2: Find the start of the loop
        slow = head
        if slow == fast:
            # Special case: Loop starts at head
            while fast.next != slow:
                fast = fast.next
        else:
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next

        # Step 3: Remove the loop
        fast.next = None
