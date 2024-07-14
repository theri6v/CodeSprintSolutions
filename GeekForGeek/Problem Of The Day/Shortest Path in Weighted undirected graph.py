#User function Template for python3
from typing import List
from collections import defaultdict, deque
import heapq

class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # code here
        adj = defaultdict(list)
        
        for edge in edges:
            src, dst, dist = edge[0], edge[1], edge[2]
            adj[src].append([dst, dist])
            adj[dst].append([src, dist])
        
        dist, parent, q = [1e9]*(n+1), [i for i in range(n+1)], [(0, 1)]
        dist[1] = 0
        
        while q:
            dis, node = heapq.heappop(q)
            if dis > dist[node]:    continue
            
            for neighbor, weight in adj[node]:
                if dis+weight < dist[neighbor]:
                    dist[neighbor] = dis+ weight
                    heapq.heappush(q, (dist[neighbor], neighbor))
                    parent[neighbor] = node
        
        
        if dist[n] == 1e9: return [-1]
        
        path, i = deque(), n
        path.append(n)
        
        sum_ = 0
        while parent[i] != i:
            i = parent[i]
            path.appendleft(i)
            
        path.appendleft(dist[n])
        return path
        
        
        
        
