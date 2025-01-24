#User function Template for python3
'''
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    
'''
# Return boolean value True or False

class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return True
        return False
