class Solution:
    def safeNodes(self, V, edges):
        from collections import deque
        outdeg = [0] * V
        rev = [[] for _ in range(V)]
        for u, v in edges:
            rev[v].append(u)
            outdeg[u] += 1
        q = deque()
        for i in range(V):
            if outdeg[i] == 0:
                q.append(i)
        safe = [False] * V
        while q:
            node = q.popleft()
            safe[node] = True
            for nei in rev[node]:
                outdeg[nei] -= 1
                if outdeg[nei] == 0:
                    q.append(nei)
        return [i for i in range(V) if safe[i]]
