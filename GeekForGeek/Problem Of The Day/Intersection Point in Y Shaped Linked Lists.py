#User function Template for python3
'''
    Function to return the value at point of intersection
    in two linked list, connected in y shaped form.
    
    Function Arguments: head_a, head_b (heads of both the lists)
    
    Return Type: value in NODE present at the point of intersection
                 or -1 if no common point.

    Contributed By: Nagendra Jha

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''

#Function to find intersection point in Y shaped Linked Lists.
class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
def intersetPoint(head1,head2):
    #code here
    def get_length(head):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length

    # Get lengths of both linked lists
    len1 = get_length(head1)
    len2 = get_length(head2)
    
    # Find the difference in lengths
    diff = abs(len1 - len2)
    
    # Advance the head of the longer list by 'diff' nodes
    if len1 > len2:
        for _ in range(diff):
            head1 = head1.next
    else:
        for _ in range(diff):
            head2 = head2.next

    # Traverse both lists together until intersection is found
    while head1 and head2:
        if head1 == head2:
            return head1.data  # Return the data at the intersection point
        head1 = head1.next
        head2 = head2.next

    return -1
