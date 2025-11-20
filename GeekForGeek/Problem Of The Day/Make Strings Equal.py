class Solution:
    def minCost(self,s,t,transform,cost):
        I=10**12;D=[[I]*26 for _ in range(26)]
        for i in range(26):D[i][i]=0
        for (a,b),v in zip(transform,cost):D[ord(a)-97][ord(b)-97]=min(D[ord(a)-97][ord(b)-97],v)
        for k in range(26):
            for i in range(26):
                if D[i][k]<I:
                    for j in range(26):
                        if D[k][j]<I:D[i][j]=min(D[i][j],D[i][k]+D[k][j])
        A=0
        for x,y in zip(s,t):
            u,v=ord(x)-97,ord(y)-97
            if u!=v:
                B=min((D[u][c]+D[v][c] for c in range(26) if D[u][c]<I and D[v][c]<I),default=I)
                if B==I:return-1
                A+=B
        return A
