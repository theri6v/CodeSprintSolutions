#User function Template for python3
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        """
        Perform a breadth-first search traversal of the graph.
    
        Args:
            adj: 2-D adjacency list where adj[i] represents the list of vertices connected to vertex i
        
        Returns:
            A list containing the BFS traversal of the graph
        """
        if not adj:
            return []
    
        n = len(adj)  # Number of vertices
        visited = [False] * n
        result = []
    
        # Create a queue for BFS
        queue = []
    
        # Start BFS from vertex 0
        queue.append(0)
        visited[0] = True
    
        while queue:
            # Dequeue a vertex from queue
            vertex = queue.pop(0)
            result.append(vertex)
        
            # Get all adjacent vertices of the dequeued vertex
            # If an adjacent has not been visited, mark it visited and enqueue it
            for neighbor in adj[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
    
        return result
