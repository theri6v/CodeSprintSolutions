#User function Template for python3
class Solution:
    def minOperations(self, str1, str2):
        def f(i, j):
            if i < 0 or j < 0:
                return 0  
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            if str1[i] == str2[j]:
                dp[(i, j)] = 1 + f(i - 1, j - 1)
            else:
                dp[(i, j)] = max(f(i - 1, j), f(i, j - 1))
            
            return dp[(i, j)]
        
        m, n = len(str1), len(str2)
        dp = {}
        lcs_length = f(m - 1, n - 1)
        return (m - lcs_length) + (n - lcs_length)  
