class Solution:
    def findGreater(self, arr):
        from collections import Counter
        cnt=Counter(arr)
        ret=[-1]*len(arr)
        stk=[]
        for ix,ve in enumerate(arr):
            while stk and cnt[arr[stk[-1]]]<cnt[ve]:
                ret[stk[-1]]=ve
                stk.pop()
            stk.append(ix)
        return ret
