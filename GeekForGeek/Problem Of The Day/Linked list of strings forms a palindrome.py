#User function Template for python3

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
def compute(head): 
    #return True/False
   
    # Step 1: Traverse the linked list to combine the string data
    current = head
    combined_string = ""
    while current:
        combined_string += current.data
        current = current.next
    
    # Step 2: Check if the combined string is a palindrome
    return combined_string == combined_string[::-1]


