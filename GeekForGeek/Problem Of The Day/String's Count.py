#User function Template for python3

class Solution:
    def countStr(self, n):
        if n == 1:
            return 3
        if n == 2:
            return 8
        
        ans = (n * n * n + 3 * n + 2) // 2
        return ans
        
