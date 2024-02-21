#User function Template for python3

from functools import lru_cache

class Solution:
    def countWays(self, n, s):
        mod = 1003
        exp = s
        @lru_cache(maxsize=None)
        def recur(requirement, l, r):
            if abs(l-r) == 1:
                if exp[l] == requirement:
                    return 1
                else:
                    return 0
                
            res = 0
            for i in range(l, r):
                if not exp[i].isalpha():
                    lt = recur('T', l, i)
                    lf = recur('F', l, i)
                    rt = recur('T', i+1, r)
                    rf = recur('F', i+1, r)
                    if exp[i] == '&':
                        if requirement == 'T':
                            res += lt * rt
                        else:
                            res += (lf * rf) + (lf * rt) + (lt * rf)
                    elif exp[i] == '|':
                        if requirement == 'T':
                            res += (lt * rt) + (lf * rt) + (lt * rf)
                        else:
                            res += lf * rf
                    elif exp[i] == '^':
                        if requirement == 'T':
                            res += (lf * rt) + (lt * rf)
                        else:
                            res += (lf * rf) + (lt * rt)
            
            return res % mod
        
        return recur('T', 0, n) % mod
