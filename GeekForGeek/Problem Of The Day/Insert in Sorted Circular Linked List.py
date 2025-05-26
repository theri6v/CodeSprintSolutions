class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)

        # Case 1: Empty list
        if not head:
            new_node.next = new_node
            return new_node

        current = head
        while True:
            # Case 2a: Inserting between two nodes
            if current.data <= data <= current.next.data:
                break
            # Case 2b: At the turning point from max to min
            if current.data > current.next.data:
                if data >= current.data or data <= current.next.data:
                    break
            current = current.next
            # Full loop done, insert anywhere
            if current == head:
                break

        # Insert new_node after current
        new_node.next = current.next
        current.next = new_node

        # Return new head (update only if inserted before head)
        return head if head.data <= data else new_node
