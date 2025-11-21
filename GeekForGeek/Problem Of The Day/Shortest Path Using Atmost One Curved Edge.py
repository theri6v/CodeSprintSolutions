class Solution:
    def shortestPath(self, V, a, b, edges):
        from heapq import heappop, heappush
        graph = [[] for _ in range(2 * V)]
        for u, v, w1, w2 in edges:
            u2, v2 = u + V, v + V
            # First "sub graph"
            graph[u].append((v, w1))
            graph[v].append((u, w1))
            # Second, mirror "sub graph"
            graph[u2].append((v2, w1))
            graph[v2].append((u2, w1))
            # Add directed, "curved" edge
            # from the first to the second "sub graph"
            graph[u].append((v2, w2))
            graph[v].append((u2, w2))
        visited = [False] * (2 * V)
        h = [(0, a)]
        end_nodes = (b, b + V)
        while h:
            dist, u = heappop(h)
            if visited[u]:
                continue
            visited[u] = True
            if u in end_nodes:
                return dist
            for v, weight in graph[u]:
                if not visited[v]:
                    heappush(h, (dist + weight, v))
        return -1
