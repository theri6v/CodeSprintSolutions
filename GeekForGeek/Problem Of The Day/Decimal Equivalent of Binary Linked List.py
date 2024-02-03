# your task is to complete this function
# Function should return an integer value

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def decimalValue(self, head):
        MOD=10**9+7
        res=0
        while head:
            res=(res*2+head.data)%MOD
            head=head.next
        return res
