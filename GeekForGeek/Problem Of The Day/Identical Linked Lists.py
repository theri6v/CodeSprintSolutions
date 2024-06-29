# your task is to complete this function
# function should return true/1 if both
# are identical else return false/0
'''
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
'''

#Function to check whether two linked lists are identical or not.
def areIdentical(head1, head2):
    curr1 = head1
    curr2 = head2
    while curr1 and curr2:
        if curr1.data != curr2.data:
            return False
        curr1 = curr1.next
        curr2 = curr2.next
    if curr1 == None and curr2 == None:
        return True
    else:
        return False
