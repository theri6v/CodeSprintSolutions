# your task is to complete this function

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        tmp = head
        node_count = 0
        while tmp:
            tmp = tmp.next
            node_count += 1
            
        mid_node_pos = (node_count//2) + 1
        mid_node = 0
        
        while head:
            mid_node_pos -= 1
            if mid_node_pos == 0:
                mid_node = head
                break
            head = head.next
            
        return mid_node.data
            
        
        # Code here
        # return the value stored in the middle node
