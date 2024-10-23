#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def sumOfLastN_Nodes(self, head, n):
        # Initialize two pointers
        first = head
        second = head
        
        # Move the first pointer n steps ahead
        for _ in range(n):
            first = first.next
        
        # Move both pointers until the first pointer reaches the end
        while first is not None:
            first = first.next
            second = second.next
        
        # Now second is at the start of the last n nodes, calculate the sum
        total_sum = 0
        while second is not None:
            total_sum += second.data
            second = second.next
        
        return total_sum
