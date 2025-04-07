class Solution:
    def isCycle(self, V, edges):
        # code here
         # Create in-degree list for each vertex
        in_degree = [0] * V
        # Create adjacency list representation of the graph
        graph = [[] for _ in range(V)]
        
        # Build the graph and calculate in-degree of nodes
        for edge in edges:
            graph[edge[0]].append(edge[1])
        for node_list in graph:
            for node in node_list:
                in_degree[node] += 1
        
        # Initialize a queue with nodes having in-degree of 0
        queue = []
        for i in range(V):
            if in_degree[i] == 0:
                queue.append(i)
        
        # Perform Topological Sort
        sorted_nodes = []
        while queue:
            current = queue.pop(0)
            sorted_nodes.append(current)
            for adjacent in graph[current]:
                in_degree[adjacent] -= 1
                if in_degree[adjacent] == 0:
                    queue.append(adjacent)
        
        # Check if all nodes were sorted
        return len(sorted_nodes) < V
 
