#User function Template for python3

'''
class Node: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  '''
class Solution:
    def sortedInsert(self, head, data):
    #     #code here
    #     prev = head
    #     head = head.next
    #     inserted = False
    #     while not inserted and head:
    #         if data >= prev.data and data < head.data:
    #             add = Node(data)
    #             prev.next= add
    #             add.next = head
    #             inserted = True
    #         else:
    #             prev = prev.next
    #             head = head.next
    
        new_node = Node(data)
    
        if not head:
            new_node.next = new_node
            return new_node
        current = head
        if data < head.data:
            while current.next!=head:
                current=current.next
            current.next=new_node
            new_node.next=head
            return new_node
    
        current = head
        while current.next!= head and current.next.data < data:
            current = current.next
    
        new_node.next = current.next
        current.next = new_node
    
        return head
