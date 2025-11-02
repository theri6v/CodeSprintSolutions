class Solution:
    def maxEdgesToAdd(self, V, edges):
        # code here
        return (V*(V-1))//2-len(edges)
