# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    def rotate(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        temp = head
        while temp.next:
            temp = temp.next
            length += 1
        
        k = k % length
        if k == 0:
            return head
            
        temp.next = head
        
        newTail = head
        for i in range(1, k):
            newTail = newTail.next
        
        newHead = newTail.next
        newTail.next = None # breaking the circular connection
        return newHead
        
