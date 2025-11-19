class Solution:
    def minCostPath(self, m):
        import heapq
        h, w = len(m), len(m[0])
        dist = [[float('inf')]*w for _ in range(h)]
        pq = [(0, 0, 0)]
        dist[0][0] = 0

        while pq:
            d, x, y = heapq.heappop(pq)
            if (x, y) == (w-1, h-1): return d
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < w and 0 <= ny < h:
                    nd = max(d, abs(m[ny][nx] - m[y][x]))
                    if nd < dist[ny][nx]:
                        dist[ny][nx] = nd
                        heapq.heappush(pq, (nd, nx, ny))
