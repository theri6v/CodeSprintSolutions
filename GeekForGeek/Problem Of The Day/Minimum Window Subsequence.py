class Solution:
    def minWindow(self, s1, s2):
        n,m=len(s1),len(s2)
        inf = 10**9
        dp = {}
        
        def solve(i,j):
            if j==m:
                return i
            
            if i==n:
                return inf
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            if s1[i]==s2[j]:
                dp[(i,j)] = solve(i+1,j+1)
            else:
                dp[(i,j)] = solve(i+1,j)
            return dp[(i,j)]
        
        start=-1
        min_ = inf
        
        for i in range(n):
            if s1[i]==s2[0]:
                end = solve(i,0)
                if end!=inf and end-i<min_:
                    min_ = end-i
                    start = i
        
        return "" if start==-1 else s1[start:start+min_]
