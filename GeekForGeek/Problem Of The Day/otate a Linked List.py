class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    
    # Function to rotate a linked list.
    def rotate(self, head, k):
        # Edge case: if the head is None or k is 0, return the head as is.
        if not head or k == 0:
            return head
        
        # Step 1: Find the length of the linked list
        current = head
        length = 1
        while current.next:
            current = current.next
            length += 1
        
        # Step 2: Update k if k is greater than or equal to length
        k = k % length
        if k == 0:
            return head
        
        # Step 3: Find the k-th node
        current = head
        for i in range(k - 1):
            current = current.next
        
        # Step 4: The k-th node will be the new tail, and the node after it will be the new head
        new_head = current.next
        current.next = None
        
        # Step 5: Find the end of the rotated part and link it to the original head
        end_node = new_head
        while end_node.next:
            end_node = end_node.next
        end_node.next = head
        
        # Return the new head
        return new_head

