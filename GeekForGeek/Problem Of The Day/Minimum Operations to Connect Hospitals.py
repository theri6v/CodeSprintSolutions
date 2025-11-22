from collections import defaultdict

class Solution:
    def dfs(self,node,visited,graph):
        visited[node]=1
        
        for n in graph[node]:
            if not visited[n]:
                self.dfs(n,visited,graph)
    
    def minConnect(self, V, edges):
        E = len(edges)
        
        if E<V-1:
            return -1
        
        graph = defaultdict(list)
        
        for r,c in edges:
            graph[r].append(c)
            graph[c].append(r)
        
        components = 0
        
        visited = [0]*V
        
        for i in range(V):
            if not visited[i]:
                self.dfs(i,visited,graph)
                components+=1
        
        return components-1
