#function Template for python3

"""
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    def reverseList(self, head):
        prev = None  # This will become the new head
        curr = head  # Start from the current head of the list
        while curr:
            next_node = curr.next  
            curr.next = prev     
            prev = curr
            curr = next_node   
        return prev
