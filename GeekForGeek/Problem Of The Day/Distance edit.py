class Solution:
    def editDistance(self, str1, str2):
        n = len(str1)
        m = len(str2)
        
        if not str1 or not str2:
            return max(n,m)
        
        def setUp(n, m):
            T = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
            T[0][0] = 0 
            for i in range(1, n + 1):
                T[0][i] = i
            for i in range(1, m + 1):
                T[i][0] = i
                
            return T
        
        def DP(n, m, T, s1, s2):
            
            if T[m][n] != -1:
                return T[m][n]
            
            if s1[n-1] == s2[m-1]:
                T[m][n] = DP(n-1, m-1, T, s1, s2)
                return T[m][n]
                
            else:
                T[m][n] = min(DP(n-1, m, T, s1, s2) + 1, DP(n-1, m-1, T, s1, s2) + 1, DP(n, m-1, T, s1, s2) + 1)
                return T[m][n]
                
        T = setUp(n, m)
        return DP(n, m, T, str1, str2)
            
            
