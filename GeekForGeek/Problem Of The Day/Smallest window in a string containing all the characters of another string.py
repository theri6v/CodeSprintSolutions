#User function Template for python3


class Solution:
    def smallestWindow(self, s, p):
        k = len(s)
        m = set(p)
        n = set(s)
        pc = {i: p.count(i) for i in m}
        sc = {i: s.count(i) for i in n}
        cc = {}
        l = sum(pc.values())
        count = 0
        ans = ""
        small = []
        i = 0
        j = 0
        while j < k:
            while count != l and j < k:
                if s[j] not in m:
                    ans = ans + s[j]
                else:
                    ans = ans + s[j]
                    cc[s[j]] = cc.get(s[j], 0) + 1
                    if cc[s[j]] <= pc[s[j]]:
                        count += 1
                j += 1        
            if count == l:
                small.append(ans)
            
            while count == l:
                if s[i] not in m:
                    ans = ans[1:]
                    i += 1
                else:
                    cc[s[i]] -= 1
                    if cc[s[i]] < pc[s[i]]:
                        small.append(ans)
                        ans = ans[1:]    
                        count -= 1
                        i += 1
                        break
                    else:
                        ans = ans[1:]
                        i += 1
        if count == l:
            small.append(ans)        
        if len(small) == 0:
            return "-1"
        h = ""
        d = 10000000
        for i in small:
            if len(i) < d:
                h = i
                d = len(i)
        return h 
