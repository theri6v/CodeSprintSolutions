from collections import defaultdict
from functools import cache
class Solution:
    def countPaths(self, edges, V, src, dest):
        #Code here
        graph=defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
        
        @cache
        def dfs(node):
            if node==dest:
                return 1
            ans=0
            for nex in graph[node]:
                ans+=dfs(nex)
            return ans
        
        return dfs(src)
