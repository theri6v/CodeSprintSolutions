class Solution:
    def minCost(self, heights, cost):
        def cost_func(n, h, c, dh):
            l = 0
            for i in range(n):
                l += abs(h[i]-dh) * cost[i]
            return l
             
        n = len(heights)
        lo, hi = min(heights), max(heights)
        while lo <= hi:
            m = (lo + hi) // 2
            a,b,c = cost_func(n, heights, cost, m + 1), cost_func(n, heights, cost, m), cost_func(n, heights, cost,m - 1)
             
            if b <= a and b <= c:
                return b
            elif b < c:
                lo = m + 1
            else:
                hi = m - 1
                 
        return -1
