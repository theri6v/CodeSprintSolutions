#User function Template for python3

# return 1 in case of True and 0 in case of False
class Solution:
    def isAdditiveSequence(self, n):
        def check(n1, n2, s):
            if not s:
                return True
            n = n1+n2
            ns = str(n)
            if not s.startswith(ns):
                return False
            return check(n2, n, s[len(ns):])
        n = len(s)
        for i in range(1, n):
            for j in range(i+1, n):
                n1, n2 = int(s[:i]), int(s[i:j])
                if check(n1, n2, s[j:]):
                    return 1
        return 0
