class Solution:
    def countSubarrays(self, arr):
        ret=0
        stk=[]
        for ve in arr:
            while stk and stk[-1]>ve:
                stk.pop()
            stk.append(ve)
            ret+=len(stk)
        return ret
