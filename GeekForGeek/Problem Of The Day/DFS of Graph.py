class Solution:
    
    # Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        def dfs_helper(node):
            visited.add(node)
            result.append(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs_helper(neighbor)
                    
        visited = set()
        result = []
        dfs_helper(0)  # Start DFS from vertex 0
        return result

