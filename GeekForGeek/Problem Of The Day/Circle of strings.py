#User function Template for python3
from collections import defaultdict, Counter
class Solution:
    def isCircle(self, arr):
        # code here
        g = defaultdict(list)
        indegree = Counter()
        outdegree = Counter()
        for s in arr:
            g[s[0]].append(s[-1])
            indegree[s[-1]]+=1
            outdegree[s[0]] +=1
        if indegree!=outdegree:
            return 0
        
        visited = set()
        
        def dfs(n,g):
            if n in visited:
                return
            visited.add(n)
            for nbr in g[n]:
                dfs(nbr,g)
        
        dfs(arr[0][0],g)
        if len(visited)!=len(g):
            return 0
        return 1
