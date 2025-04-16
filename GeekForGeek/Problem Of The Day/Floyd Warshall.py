class Solution:
    def floydWarshall(self, dist):
        #Code here
        V = len(dist)
        INF = int(1e8)
        
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    # Only update if both paths are not INF
                    if dist[i][k] != INF and dist[k][j] != INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) 
