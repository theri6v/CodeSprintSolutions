#User function Template for python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    # Function to reverse a circular linked list
    def reverse(self, head):
        if not head or head.next == head:
            return head

        prev = None
        curr = head
        next_node = None

        # Keep track of the head for making it circular at the end
        last = head
        
        while True:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
            # Break when we reach the original head
            if curr == head:
                break

        # Fix the circular link
        last.next = prev
        head = prev

        return head        #code here
        
    # Function to delete a node from the circular linked list
    def deleteNode(self, head, key):
        if not head:
            return None
        
        # Case when list has only one node
        if head.data == key and head.next == head:
            return None
        
        # Initialize variables to find the node to be deleted
        curr = head
        prev = None
        
        # If head needs to be deleted
        if head.data == key:
            while curr.next != head:
                curr = curr.next
            curr.next = head.next
            head = head.next
            return head
        
        # Find the key in the linked list
        while curr.next != head and curr.data != key:
            prev = curr
            curr = curr.next
        
        # If key was found in the list
        if curr.data == key:
            prev.next = curr.next
        
        return head      #code here
        
