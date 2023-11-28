class Solution:
    def isEulerCircuitExist(self, V, adj):
        #Code here
        c=0
        
        for i in range(V):
            if len(adj[i]) % 2 != 0:
                c+=1
        if c==0:
            return 2
        
        if c==2:
            return 1
        return 0
