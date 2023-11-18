#User function Template for python3

''' structure of node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''

class Solution:
    def findIntersection(self,head1,head2):
    #return head
        new_node = Node(0)
        temp = new_node
        curr1 = head1
        curr2 = head2
        while curr1 and curr2:
            if curr1.data == curr2.data:
                temp.next = Node(curr1.data)
                temp = temp.next
                curr1 = curr1.next
                curr2 = curr2.next
            elif curr1.data < curr2.data:
                curr1 = curr1.next
            else:
                curr2 = curr2.next
        return new_node.next
