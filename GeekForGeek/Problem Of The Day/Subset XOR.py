class Solution:
    def subsetXOR(self, n : int):
        x = 0
        for i in range(1, n + 1):
            x ^= i
        if x == n:
            return [i for i in range(1, n + 1)]
            
        k = x ^ n
        
        if 1 <= k <= n:
            return [i for i in range(1, n + 1) if i != k]
            
        return [i for i in range(1, n)]
