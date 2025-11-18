import heapq

class Solution:
    def countPaths(self, V, edges):
        MOD = 10**9 + 7
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        dist = [float('inf')] * V
        count = [0] * V
        dist[0] = 0
        count[0] = 1
        heap = [(0, 0)]

        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]: continue
            for v, w in adj[u]:
                new_d = d + w
                if new_d < dist[v]:
                    dist[v] = new_d
                    count[v] = count[u]
                    heapq.heappush(heap, (new_d, v))
                elif new_d == dist[v]:
                    count[v] = (count[v] + count[u]) % MOD

        return count[V - 1]
