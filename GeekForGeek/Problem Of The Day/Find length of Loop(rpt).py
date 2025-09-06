class Solution:
    def lengthOfLoop(self, head):
        dic={}
        i=0
        cur=head
        while cur:
            if cur in dic:
                return abs(dic[cur]-i)
            dic[cur]=i
            i+=1
            cur=cur.next
        return 0
