#User function Template for python3
class Solution:
    def isSumString (ob,s):
        n = len(s)
        def check(i, j, k):
            nonlocal s, n
            if k == n:
                return True
            if k > n:
                return False
            n1 = int(s[i:j])
            n2 = int(s[j:k])
            ns = str(n1+n2)
            if not s[k:].startswith(ns):
                return False
            return check(j, k, k+len(ns))
        for i in range(1, n):
            for j in range(i+1, n):
                if check(0, i, j):
                    return 1
        return 0
