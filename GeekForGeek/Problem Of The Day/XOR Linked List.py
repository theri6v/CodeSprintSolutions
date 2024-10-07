#User function Template for python3
def insert(head, data):
    new_node = Node(data)
    new_node.npx = head
    return new_node


def getList(head):
    result = []
    current = head
    while current is not None:
        result.append(current.data)
        current = current.npx
    return result
