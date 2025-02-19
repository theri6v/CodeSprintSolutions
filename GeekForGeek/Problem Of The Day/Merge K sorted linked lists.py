#User function Template for python3
'''
class Node:
    def _init_(self,x):
        self.data = x
        self.next = None
'''
class Solution:
    def mergeKLists(self, arr):
        # code here
        # return head of merged list
        n=len(arr)
        a=[]
        for i in range(n):
            p=arr[i]
            while p:
                a.append(p.data)
                p=p.next
        a.sort()
        head=Node(a[0])
        ptr=head
        for i in range(1,len(a)):
            temp=Node(a[i])
            ptr.next=temp
            ptr=ptr.next
        return head
