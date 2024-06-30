class Solution:
    def delete_node(self, head, x):
        if x == 1:
            return head.next
            
        temp = head
        
        while x>1:
            temp = temp.next
            x -= 1
            
        prv, nxt = temp.prev, temp.next
        
        del(temp)
        
        prv.next = nxt
        if nxt:
            nxt.prev = prv
        
        return head
