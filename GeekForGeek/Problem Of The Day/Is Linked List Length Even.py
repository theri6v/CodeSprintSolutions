class Solution:
    # your task is to complete this function
    # function should return false if length is even
    # else return true
    def isLengthEven(self, head):
        # Code here
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count % 2 == 0
