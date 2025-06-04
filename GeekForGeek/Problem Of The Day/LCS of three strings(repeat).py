class Solution:
    def lcsOf3(self,s1, s2, s3):
        l1=len(s1)
        l2=len(s2)
        l3=len(s3)
        dp=[[[0]*(l1+1) for _ in range(l2+1)] for _ in range(l3+1)]
        for i1 in range(1,l1+1):
            for i2 in range(1,l2+1):
                for i3 in range(1,l3+1):
                    if s1[i1-1]==s2[i2-1] and s2[i2-1]==s3[i3-1]:
                        dp[i3][i2][i1]=dp[i3-1][i2-1][i1-1]+1
                        continue
                    dp[i3][i2][i1]=max(dp[i3-1][i2][i1],dp[i3][i2-1][i1],dp[i3][i2][i1-1])
        return dp[-1][-1][-1]
