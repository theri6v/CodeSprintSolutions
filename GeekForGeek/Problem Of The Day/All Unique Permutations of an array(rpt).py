class Solution:
    def uniquePerms(self, arr):
        lth=len(arr)
        seen=set()
        cur=[]
        ret=[]
        def bt(bm=(1<<lth)-1):
            nonlocal arr,lth,seen,cur
            if tuple(cur) in seen:
                return
            seen.add(tuple(cur))
            if bm==0:
                ret.append(cur[:])
                return
            for ix in range(lth):
                if (1<<ix)&bm:
                    cur.append(arr[ix])
                    bt((1<<ix)^bm)
                    cur.pop()
        bt()
        return sorted(ret)
