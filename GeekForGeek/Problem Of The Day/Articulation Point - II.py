class Solution:
    def articulationPoints(self, V, edges):
        # code here
        
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def findPoint(adj, u, visited, disc, low, time, parent, isAp):
  
            time[0] += 1
            visited[u] = 1
            disc[u] = low[u] = time[0]
            children = 0
            
            for v in adj[u]:
                if not visited[v]:
                    children += 1
                    findPoint(adj, v, visited, disc, low, time, u, isAp)
                    
                    low[u] = min(low[u], low[v])
                    
                    if parent != -1 and low[v] >= disc[u]:
                        isAp[u] = 1
                elif v != parent:
                    low[u] = min(low[u], disc[v])
            if parent == -1 and children > 1:
                isAp[u] = 1
        disc = [0] * V
        low = [0] * V
        visited = [0] * V
        isAp = [0] * V
        time = [0]
        
        for i in range(V):
            if not visited[i]:
                findPoint(adj, i, visited, disc, low, time, -1, isAp)
        result = [i for i in range(V) if isAp[i]]
        return result if result else [-1]
        
