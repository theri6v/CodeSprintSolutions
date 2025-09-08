#User function Template for python3

'''
    :param head: head of unsorted linked list 
    :return: head of sorted linkd list
    
    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
'''
class Solution:
    #Function to sort the given linked list using Merge Sort.
    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.data < right.data:
            merged_head = left
            merged_head.next = self.merge(left.next, right)
        else:
            merged_head = right
            merged_head.next = self.merge(left, right.next)

        return merged_head

    # Function to find the middle of the linked list.
    def findMiddle(self, head):
        if not head:
            return None
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    # Function to perform Merge Sort on the linked list.
    def mergeSort(self, head):
        if not head or not head.next:
            return head

        middle = self.findMiddle(head)
        left_half = head
        right_half = middle.next
        middle.next = None

        left_sorted = self.mergeSort(left_half)
        right_sorted = self.mergeSort(right_half)

        sorted_list = self.merge(left_sorted, right_sorted)

        return sorted_list

# Helper function to create a linked list from a list of values.
def createLinkedList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

