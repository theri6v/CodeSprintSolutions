from itertools import accumulate
class Solution:
    def maxScore(self, s, jumps):
        pre = list(accumulate(map(ord, s), initial=0))
        adj = defaultdict(list)
        for u, v in jumps:
            adj[u].append(v)
        
        n = len(s)
        dp = [0]*(n+1)
        pos = {s[n-1]: n-1}
        for i in range(n-2, -1, -1):
            for u in adj[s[i]]:
                if j := pos.get(u):
                    dp[i] = max(dp[i], dp[j] + pre[j] - pre[i])
            if j := pos.get(s[i]):
                dp[i] = max(dp[i], dp[j] + pre[j] - pre[i+1])
            pos[s[i]] = i
        return dp[0]
