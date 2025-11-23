class Solution:
    def maxRemove(self, stones):
        # Code here
        parent = {}
        rank = {}

        def find(u):
            # Path compression
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            # Initialize if not present
            if u not in parent:
                parent[u] = u
                rank[u] = 0
            if v not in parent:
                parent[v] = v
                rank[v] = 0

            pu, pv = find(u), find(v)
            if pu == pv:
                return
            # Union by rank
            if rank[pu] < rank[pv]:
                parent[pu] = pv
            elif rank[pu] > rank[pv]:
                parent[pv] = pu
            else:
                parent[pv] = pu
                rank[pu] += 1

        # Union row index with column index (using negative for column)
        for x, y in stones:
            union(x, ~y)   # use bitwise NOT (~y) instead of -y to avoid collision

        # Count distinct connected components
        unique_roots = {find(u) for u in parent}
        return len(stones) - len(unique_roots)
