#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def countNodesInLoop(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # Cycle detected
            if slow == fast:
                return self.countLoopLength(slow)

        return 0  # No loop

    def countLoopLength(self, meeting_point):
        current = meeting_point
        count = 1
        while current.next != meeting_point:
            count += 1
            current = current.next
        return count
