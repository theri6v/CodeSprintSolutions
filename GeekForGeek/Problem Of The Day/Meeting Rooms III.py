from heapq import heappush,heappop
from collections import Counter
class Solution:
    def mostBooked(self, n, meetings):
        #sam
        room = [i for i in range(n)]
        used = []
        count = Counter()
        
        for start,end in sorted(meetings):
            
            #for empty the room.
            while used and used[0][0]<=start:
                _,r = heappop(used)
                heappush(room,r)
            
            if room:
                r = heappop(room)
                heappush(used,(end,r))
            else:
                u_end,r = heappop(used)
                heappush(used,((u_end-start+end),r))
            
            count[r]+=1
                
        # print(count)
        mx = 0
        ans = -1
        for k,v in count.items():
            # print(k,v)
            if mx<v:
                mx = v
                ans = k
                
        return ans
