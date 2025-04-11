import heapq
from collections import defaultdict

class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # Step 1: Build the graph using an adjacency list
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))  # Undirected graph

        # Step 2: Initialize distance array
        dist = [float('inf')] * V
        dist[src] = 0

        # Step 3: Min-heap priority queue: (distance, node)
        heap = [(0, src)]

        while heap:
            current_dist, u = heapq.heappop(heap)

            if current_dist > dist[u]:
                continue

            for neighbor, weight in graph[u]:
                if dist[u] + weight < dist[neighbor]:
                    dist[neighbor] = dist[u] + weight
                    heapq.heappush(heap, (dist[neighbor], neighbor))

        return dist
