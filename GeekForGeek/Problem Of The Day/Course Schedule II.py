from collections import deque
class Solution:
    def findOrder(self, n, prerequisites):
        adj=[[] for _ in range(n)]
        indegree=[0]*n
        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u]+=1
        q=deque()
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
        ans=[]
        while q:
            u=q.popleft()
            ans.append(u)
            for v in adj[u]:
                indegree[v]-=1
                if indegree[v]==0:
                    q.append(v)
        return ans if len(ans)==n else []
