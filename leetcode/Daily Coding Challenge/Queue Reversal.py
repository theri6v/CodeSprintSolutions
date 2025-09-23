class Solution:
    def reverseQueue(self, q):
        l,r = 0, len(q)-1
        while l < r:
            q[l], q[r] = q[r], q[l]
            l+=1
            r-=1
        return q
