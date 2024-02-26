#User function Template for python3

class Solution:
    def AllPossibleStrings(self, s):
        # Code here
        res = []
        
        def solve(st, i):
            if i == len(s):
                return
            
            res.append(st+s[i])
            
            solve(st+s[i], i+1)
            solve(st, i+1)
        
        solve("", 0)
        return sorted(res)
