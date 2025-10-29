class Solution:
    def diameter(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def bfs(start):
            dist = [-1] * V
            dist[start] = 0
            q = deque([start])
            farthest_node = start
            while q:
                node = q.popleft()
                for nei in adj[node]:
                    if dist[nei] == -1:
                        dist[nei] = dist[node] + 1
                        q.append(nei)
                        if dist[nei] > dist[farthest_node]:
                            farthest_node = nei
            return farthest_node, dist[farthest_node]
        nodeA, _ = bfs(0)
        _, diameter = bfs(nodeA)
        return diameter
