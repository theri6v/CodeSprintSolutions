class Solution:
    def validgroup(self, arr ,k):
        lth=len(arr)
        if lth%k!=0:
            return False
        from collections import Counter
        cnt=Counter(arr)
        while lth:
            mn=min(cnt)
            for ix in range(mn,mn+k):
                if ix in cnt:
                    cnt[ix]-=1
                    lth-=1
                    if cnt[ix]==0:
                        cnt.pop(ix)
                else:
                    return False
        return True
