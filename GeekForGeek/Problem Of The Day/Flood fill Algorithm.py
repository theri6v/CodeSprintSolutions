class Solution:
    def floodFill(self, image, sr, sc, newColor):
        #Code here
        a=[-1,0,1,0]
        b=[0,1,0,-1]
        old=image[sr][sc]
        n=len(image)
        m=len(image[0])
        vis=[[0]*m for _ in range(n)]
        def dfs(sr,sc):
            vis[sr][sc]=1
            image[sr][sc]=newColor
            for i in range(4):
                nr=sr+a[i]
                nc=sc+b[i]
                if 0<=nr<n and 0<=nc<m and vis[nr][nc]==0 and image[nr][nc]==old:
                    dfs(nr,nc)
        dfs(sr,sc)
        return image
