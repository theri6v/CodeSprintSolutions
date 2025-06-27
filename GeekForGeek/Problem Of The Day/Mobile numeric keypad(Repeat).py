class Solution:
	def getCount(self, n):
		if n == 1:
            return 10
        jumps = [ [0,8],[1,2,4],[2,1,3,5],[3,2,6],[4,1,5,7],[5,2,4,6,8],
        [6,3,5,9],[7,4,8],[8,5,7,9,0],[9,8,6]
        ]
        dp = [1] * 10
        for _ in range(n-1):
            nextDp = [0] * 10
            for n in range(10):
                for j in jumps[n]:
                    nextDp[j] = (nextDp[j] + dp[n]) 
            dp = nextDp
        # print(dp)
        return sum(dp) 
