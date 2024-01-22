#User function Template for python3

from collections import deque, defaultdict

class Solution:
    def findOrder(self, n, m, prerequisites):
        indegree = [0] * (n)
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
        for i in range(n):
            for j in adj[i]:
                indegree[j] += 1
        q = deque()
        count = 0
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        ans = []
        while q:
            u = q.popleft()
            ans.append(u)
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
            count += 1
        if count != n:
            return []
        ans.reverse()
        return ans
