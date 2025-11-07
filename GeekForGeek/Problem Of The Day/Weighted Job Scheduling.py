class Solution: 
    def maxProfit(self, jobs):
        # code here
        from bisect import bisect_left
        n = len(jobs)
        jobs.sort(key=lambda j: (j[1], j[0]))
        dp = [0]*(n+1)
        for i in range(n):
            if i == 0:
                dp[i+1] = jobs[i][2]
                continue
            dp[i+1] = dp[i]
            start_time = jobs[i][0]
            j = bisect_left(jobs, start_time+1, key=lambda x: x[1])-1
            dp[i+1] = max(dp[i+1], jobs[i][2]+dp[j+1])
        return dp[-1]
