#User function Template for python3

class Solution:
    def longestPalinSubseq(self, s):
        s1 = s
        s2 = s[::-1]
        dp = [[-1]*len(s2) for _ in range(len(s1))]
        def rec(p1, p2):
            if p1 == len(s1) or p2 == len(s2):
                return 0
            if dp[p1][p2] != -1:
                return dp[p1][p2]
            
            if s1[p1] == s2[p2]:
                ma = 1 + rec(p1+1, p2+1)
            else:
                ma = max(
                    rec(p1+1, p2),
                    rec(p1, p2+1)
                )
            
            dp[p1][p2] = ma
            
            return ma
            
        return rec(0, 0)
                
