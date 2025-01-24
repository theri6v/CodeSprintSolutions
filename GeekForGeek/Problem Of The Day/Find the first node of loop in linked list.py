#User function Template for python3

""" Node Class
    class Node:
        def __init__(self, data):   # data -> value stored in node
            self.data = data
            self.next = None
"""
class Solution:
    def findFirstNode(self, head):
        if not head or not head.next:
            return None
        
        # Step 1: Detect the presence of a loop using slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # Cycle detected
                break
        else:
            return None  # No cycle
        
        # Step 2: Find the start of the loop
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return fast  # This is the start of the loop
