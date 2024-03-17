#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def countPair(self, head1, head2, n1, n2, x):
        arr=[]
        cnt = 0
        temp=head1
     
        while temp:
            arr.append(temp.data)
            temp=temp.next
        
        set1=set(arr)
        temp2=head2
        while temp2:
            if x-temp2.data in set1:
                cnt+=1
            temp2=temp2.next
        
        return cnt
        '''
        head1:  head of linkedList 1
        head2:  head of linkedList 2
        n1:  len of  linkedList 1
        n2:  len of linkedList 1
        x:   given sum
        '''
