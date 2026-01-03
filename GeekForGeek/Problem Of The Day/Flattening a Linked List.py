class Solution:
    def flatten(self, root):
        dummy=Node(0)
        cur=dummy
        import heapq
        cnt=0
        hp=[(root.data,cnt,root,)]
        while hp:
            ve,_,node=heapq.heappop(hp)
            if node.next!=None:
                cnt+=1
                heapq.heappush(hp,(node.next.data,cnt,node.next,))
            if node.bottom!=None:
                cnt+=1
                heapq.heappush(hp,(node.bottom.data,cnt,node.bottom,))
            cur.bottom=node
            cur=cur.bottom
        return dummy.bottom
