#User function Template for python3


from typing import List

import heapq

class Solution:
    def dijkstra(self, curr, n, distThreshold, graph):
        pq = []
        heapq.heappush(pq, (0, curr))
        
        vis = [0] * n
        cnt = 0
        
        while pq:
            dist, node = heapq.heappop(pq)
            
            if vis[node]:
                continue
                
            vis[node] = 1
            if dist > distThreshold:
                continue
            cnt += 1
            
            for nodeDist, nextNode in graph[node]:
                if not vis[nextNode]:
                    heapq.heappush(pq, (dist + nodeDist, nextNode))
        
        return cnt
    
    def findCity(self, n, m, edges, distThreshold):
        graph = [[] for _ in range(n)]
        
        for edge in edges:
            graph[edge[0]].append((edge[2], edge[1]))
            graph[edge[1]].append((edge[2], edge[0]))
        
        out = -1
        nax = float('inf')
        
        for i in range(n):
            cnt = self.dijkstra(i, n, distThreshold, graph)
            
            if cnt <= nax:
                nax = cnt
                out = i
        
        return out

