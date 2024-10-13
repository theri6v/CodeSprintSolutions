#User function Template for python3

'''class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  
        self.next = None'''

class Solution:
    def deleteAlt(self, head):
        
        if head is None:
            return
    
        current = head
        while current and current.next:
            next_node = current.next  # The node to be deleted
            current.next = next_node.next  # Bypass the next node
            current = current.next
