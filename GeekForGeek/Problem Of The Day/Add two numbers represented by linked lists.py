#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, num1, num2):
        # code here
        # return head of sum list
        
        prev,curr1,curr2 = None,num1,num2
        
        while curr1:
            nxt = curr1.next
            curr1.next = prev
            prev = curr1
            curr1 = nxt
            
        num1 = prev
        prev = None
        
        while curr2:
            nxt = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = nxt
            
        num2 = prev
        
        curr1,curr2,carry,result = num1,num2,0,Node(0)
        ans = result
        
        while (curr1 or curr2 or carry == 1):
            sm = 0
            
            if curr1:
                sm += curr1.data
                curr1 = curr1.next
                
            if curr2:
                sm += curr2.data
                curr2 = curr2.next
                
            sm += carry
            ans.next = Node(sm%10)
            carry = sm//10
            ans = ans.next
            
            
        prev = None
        ans = result.next
        
        while ans:
            nxt = ans.next
            ans.next = prev
            prev = ans
            ans = nxt
            
        result = prev
        
        
        while result.data == 0 and result.next: result = result.next
        
        return result
