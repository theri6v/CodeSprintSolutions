#User function Template for python3

class Solution:
    def maximumWeight(self, n, edges, q, queries):
        # code here
        
        store = [i for i in range(n+1)]
        sz = [1 for _ in range(n+1)]
        sz[0] = 0
        
        def find(i):
            if store[i] != i:
                store[i] = find(store[i])
            return store[i]
            
        
        edges.sort(key=lambda x: x[2])

        queries = sorted(enumerate(queries), key=lambda x: x[1])
        
        ans = [0]*len(queries)
        start = 0
        acc = 0
        for i, q in queries:
            while start < len(edges) and edges[start][2] <= q:
                x, y, _ = edges[start]
                rx, ry = find(x), find(y)
                if rx != ry:
                    acc += sz[rx]*sz[ry]
                    sz[rx] += sz[ry]
                    sz[ry] = 0
                    store[ry] = rx
                start += 1
            ans[i] = acc
        
        return ans

