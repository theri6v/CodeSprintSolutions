class Solution:
    def swapKth(self, head, k):
        # code here
        
        ptr=head
        val=0
        while ptr:
            val+=1
            if val==k:
                break
            ptr=ptr.next
        
        if ptr is None:
            return head
            
        slow=head
        fast=head
        while k>0 and fast:
            fast=fast.next
            k-=1
            
        while fast:
            slow=slow.next
            fast=fast.next
        slow.data,ptr.data=ptr.data,slow.data
        
        return head
