
class Solution:
    def isCycle(self, V, edges):
        visit=[0]*V
        adj=[[] for i in range(V)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        st=[0]
        while len(st)>0:
            a=st.pop(0)
            visit[a]=2
            for i in adj[a]:
                if visit[i]==1:
                    return True
                elif visit[i]==0:
                    visit[i]=1
                    st.append(i)
                    
        return False
