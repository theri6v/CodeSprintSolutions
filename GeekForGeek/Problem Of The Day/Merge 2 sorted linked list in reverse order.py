'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''

# Node class to define linked list nodes

class Solution:
    def mergeResult(self, h1, h2):
        a=[]
        cur=h1
        cur2=h2
        while(cur):
            a.append(cur.data)
            cur=cur.next
        while(cur2):
            a.append(cur2.data)
            cur2=cur2.next
        a.sort()
        a=a[::-1]
        dum=Node(0)
        ans=dum
        for i in a:
            ans.next=Node(i)
            ans=ans.next
        return dum.next
