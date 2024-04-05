class Solution:

    #Function to count number of ways to reach the nth stair
    #when order does not matter.
    def countWays(self, n):

        mod = 1000000007
        dp = [0 for i in range(n + 1)]

        #base cases
        dp[0] = 1
        dp[1] = 1

        #storing number of ways to reach the ith index as
        #number of ways to reach (i-2)th index +1.
        for i in range(2, n + 1):
            dp[i] = (dp[i - 2] % mod + 1) % mod

        #returning the result.
        return dp[n]
