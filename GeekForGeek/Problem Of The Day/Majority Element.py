#User function template for Python 3

class Solution:
    def majorityElement(self, a):
        count = cand = 0
        for v in a:
            if not count:
                cand = v
            count += 1 if v == cand else -1
        return cand if sum(1 for v in a if v == cand) > len(a)//2 else -1
