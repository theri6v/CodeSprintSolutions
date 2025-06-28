from bisect import bisect_right
class Solution:
    def countLessEq(self, a, b):
        b.sort()  
        r = []
        for x in a:
            count = bisect_right(b, x)
            r.append(count)
        return r
