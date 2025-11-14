class Solution:
    def mergeStones(self, stones, k):
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1

        # Prefix sum for quick range-sum queries
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stones[i]

        def get_sum(l, r):
            return pref[r + 1] - pref[l]

        INF = 10**15
        
        # dp[i][j] = minimum cost to merge stones[i..j] into ( (j-i) % (k-1) + 1 ) piles
        dp = [[0] * n for _ in range(n)]

        # len is the segment length
        for length in range(k, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = INF

                # Try merging subsegments
                for mid in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid+1][j])

                # If this range can be merged into 1 pile, add the sum cost
                if (length - 1) % (k - 1) == 0:
                    dp[i][j] += get_sum(i, j)

        return dp[0][n-1]
