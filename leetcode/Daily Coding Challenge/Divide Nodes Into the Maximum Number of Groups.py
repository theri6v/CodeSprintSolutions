from collections import defaultdict, deque
from typing import List

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            component_nodes.append(node)
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        def bfs(start_node):
            distances = [-1] * (n + 1)
            distances[start_node] = 1
            queue = deque([start_node])
            max_distance = 1
            
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if distances[neighbor] == -1:
                        distances[neighbor] = distances[node] + 1
                        max_distance = distances[neighbor]
                        queue.append(neighbor)
                    elif abs(distances[node] - distances[neighbor]) != 1:
                        return -1  # Invalid bipartite structure
            
            return max_distance

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * (n + 1)
        total_sets = 0
        
        for i in range(1, n + 1):
            if not visited[i]:
                component_nodes = []
                dfs(i)
                max_dist = max(bfs(node) for node in component_nodes)
                if max_dist == -1:
                    return -1
                total_sets += max_dist
                
        return total_sets
