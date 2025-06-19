class Solution:
    def caseSort(self, s):
        l = iter(sorted(c for c in s if c.islower()))
        u = iter(sorted(c for c in s if c.isupper()))
        return ''.join(next(l) if c.islower() else next(u) for c in s)
