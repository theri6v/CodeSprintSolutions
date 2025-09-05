class Solution:
    def segregate(self, head):
        #code here
        temp=head
        countZero=countOne=countTwo=0
        while temp:
            if temp.data==0:
                countZero+=1
            elif temp.data==1:
                countOne+=1
            else:
                countTwo+=1
            temp=temp.next
        temp=head
        while temp:
            if countZero!=0:
                temp.data=0
                countZero-=1
            elif countOne!=0:
                temp.data=1
                countOne-=1
            else:
                temp.data=2
                countTwo-=1
            temp=temp.next
        return head
