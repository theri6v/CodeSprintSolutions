from typing import List
from heapq import heappop,heappush

class Solution:
    def MinimumEffort(self, rows : int, columns : int, heights : List[List[int]]) -> int:
        # code here
        mh=[(0,0,0)]
        vis=set()
        move=[(0,1),(0,-1),(1,0),(-1,0)]
        while mh:
            val,r,c=heappop(mh)
            if (r,c) in vis:
                continue
            vis.add((r,c))
            if (r,c)==(rows-1,columns-1):
                return val
            for dr,dc in move:
                nr,nc=r+dr,c+dc
                if nr<0 or nr==rows or nc<0 or nc==columns or (nr,nc) in vis:
                    continue
                newval=max(val,abs(heights[r][c]-heights[nr][nc]))
                heappush(mh,(newval,nr,nc))
        return 0 
