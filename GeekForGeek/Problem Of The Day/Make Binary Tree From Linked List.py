# User function Template for python3

'''
class ListNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None


# Tree Node structure
class Tree:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''

#Function to make binary tree from linked list.
def convert(head):
  
    # code here
    if not head:
        return None
    
    nodes = []
    while head:
        nodes.append(head.data)
        head = head.next
    
    def buildTree(index):
        if index >= len(nodes):
            return None
        root = Tree(nodes[index])
        root.left = buildTree(2 * index + 1)
        root.right = buildTree(2 * index + 2)
        return root
    
    return buildTree(0)

