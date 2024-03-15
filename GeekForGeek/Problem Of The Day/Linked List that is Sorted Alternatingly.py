#User function Template for python3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    def sort(self, h1):
        #return head
        li=[]
        temp=h1
        while temp:
            li.append(temp.data)
            temp=temp.next
        i=0
        li.sort()
        temp2=h1
        while temp2:
            temp2.data=li[i]
            i+=1
            temp2=temp2.next
        return h1
