#User function Template for python3

class Solution:
    def sumOfDependencies(self,adj,V):
        #code here
        ans = 0
        for i in range(V):
            ans += len(adj[i])
        return ans

