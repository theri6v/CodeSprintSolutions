class Solution:
    def editDistance(self, str1, str2):
        len1, len2 = len(str1), len(str2)
        dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
    
        for i in range(len2):
            dp[0][i + 1] = i + 1
    
        for i in range(len1):
            dp[i + 1][0] = i + 1
    
        for i in range(len1):
            for j in range(len2):
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1], dp[i][j]) + 1
    
        return dp[-1][-1]
