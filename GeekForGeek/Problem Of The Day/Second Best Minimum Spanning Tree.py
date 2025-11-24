class Solution:
    def secondMST(self, V, edges):
        # code here
        
        def find(i, parent):
            if parent[i] != i:
                parent[i] = find(parent[i], parent)
            return parent[i]
        
        edges.sort(key=lambda x: x[2])
        

        def mst_tree(forbidden=set()):
            nonlocal edges, V
            parent = [i for i in range(V)]
            rank = [0]*V

            cost0 = 0
            mst = []
            
            for u, v, w in edges:
                if len(mst) == V-1:
                    break
                if (u, v) in forbidden:
                    continue
                
                r1 = find(u, parent)
                r2 = find(v, parent)
                if r1 == r2:
                    continue
                mst.append((u, v))
                cost0 += w
                if rank[r1] == rank[r2]:
                    parent[r2] = r1
                    rank[r1] += 1
                elif rank[r1] > rank[r2]:
                    parent[r2] = r1
                else:
                    parent[r1] = r2
            return mst, cost0
        mst, cost0 = mst_tree()

        ans = float('inf')
        for e in mst:
            m, c = mst_tree({e})
            if len(m) != V-1:
                continue
            if c > cost0:
                ans = min(ans, c)
        return ans if ans != float('inf') else -1
