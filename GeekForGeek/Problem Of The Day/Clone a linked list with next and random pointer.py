#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.random=None
        
param: head:  head of linkedList to copy
return: the head of the copied linked list the #output will be 1 if successfully copied
'''
class Solution:
    def copyList(self, head):
        if not head:
            return None
        
        # Step 1: Create new interleaved nodes.
        current = head
        while current:
            new_node = Node(current.data)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        
        # Step 2: Set the random pointers of the copied nodes.
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        # Step 3: Restore the original list and extract the copied list.
        current = head
        new_head = head.next
        while current:
            copy = current.next
            current.next = copy.next
            current = current.next
            if copy.next:
                copy.next = copy.next.next
        
        return new_head
    

