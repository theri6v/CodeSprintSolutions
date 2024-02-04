#User function Template for python3

class Solution:
    def subLinkedList(self, l1, l2): 
        # Code here
        # return head of difference list
        s1=''
        while l1:
            k=l1.data
            s1+=str(k)
            l1=l1.next
            
        s2=''
        while l2:
            a=l2.data
            s2+=str(a)
            l2=l2.next
        
        res=abs(int(s1)-int(s2))
        result_array = list(map(int, str(res)))
        result_head = Node(result_array[0])
        current = result_head

        for value in result_array[1:]:
            current.next = Node(value)
            current = current.next

        return result_head
