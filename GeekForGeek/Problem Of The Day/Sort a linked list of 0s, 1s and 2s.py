'''
    Function Arguments: head of the original list.
    Return Type: head of the new list formed.
    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }'''
    
class Solution:
    def segregate(self, head):
        #code here
        l=[]
        temp=head 
        while temp:
            l.append(temp.data)
            temp=temp.next 
        l.sort()
        node = Node(l[0])
        temp=node 
        for i in range(1,len(l)):
            new_node=Node(l[i])
            temp.next=new_node 
            temp=new_node 
        return node
    
