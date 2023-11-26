class Solution:
    
    #Function to find root of a node.
    def find_set(self, v, parent):
        
        #calling function recursively to get parent node.
        if(v != parent[v]):
            v = self.find_set(parent[v], parent)
        return v
        
    #Function to merge two nodes a and b.
    def union(self, x, y, parent, rank):
        
        x = self.find_set(x, parent)
        y = self.find_set(y, parent)
        if(rank[x] < rank[y]):
            [x,y] = [y,x]
        parent[y] = x
        rank[x] = rank[x] + rank[y]
     
    #Function to detect cycle using DSU in an undirected graph.    
    def detectCycle(self, V, adj):
        
        parent = [i for i in range(V)]
        rank = [1 for i in range(V)]
        s = set(tuple([-1,-1]))
        
        for u in range(V):
            
            #iterating through all edges of graph, finding subset of
            #both vertices of every edge, if both subsets are
            #same, then there is cycle in graph.
            for v in adj[u]:
                if(tuple([u,v]) in s or tuple([v,u]) in s):
                    continue
                s.add(tuple([u,v]))
                u1 = u
                v1 = v
                x = self.find_set(u1, parent)
                y = self.find_set(v1, parent)
                
                if(x == y):
                    #returning 1 if there is a cycle.
                    return 1
                    
                self.union(x, y, parent, rank)
                
        return 0
