# your task is to complete this function
# Function should return an integer value
# head1 denotes head node of 1st list
# head2 denotes head node of 2nd list

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''
class Solution:
    def multiply_two_lists(self, first, second):
        # Code here
        mod = ((10 ** 9) + 7)
        numOne = 0
        numTwo = 0
        while first is not None:
            numOne = ((numOne * 10) + first.data) % mod
            first = first.next
        while second is not None:
            numTwo = ((numTwo * 10) + second.data) % mod
            second = second.next
        num = numOne * numTwo
        result = num % mod
        return result
