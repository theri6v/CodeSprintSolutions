#User function Template for python3

 #Your task is to complete this Function \

class Solution:
    #function should return True/False
    def isInterleave(self, s1, s2, s3):
        # Code here
        dp = {}
        if len(s1)+len(s2)!=len(s3):
            return False
        
        def dfs(i,j):
            if i == len(s1) and j == len(s2):
                return True
            if (i,j) in dp:
                return dp[(i,j)]
            if i<len(s1) and s1[i] == s3[i+j] and  dfs(i+1,j):
                return True
            if j < len(s2) and s2 [j] == s3[i+j] and  dfs(i,j+1):
                return True
            dp[(i,j)]  = False
            return False
        return dfs(0,0)
