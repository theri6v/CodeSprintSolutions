#User function Template for python3
import sys
sys.setrecursionlimit(10000)

class Solution:
    def countSetBits(self,n):
        
        if n==1:
            return 1
        
        count = 0
        
        x = 0
        while (1 << x) <= n:
            x += 1
        
        x -= 1  
        
        count += x * (1 << (x - 1)) 
        
        msb = n - (1 << x) + 1
        rest = n - (1 << x)
        
        count += msb  
        
        if rest > 0:
            count += self.countSetBits(rest)
        
        return count


