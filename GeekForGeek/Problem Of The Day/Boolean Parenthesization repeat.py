#User function Template for python3
class Solution:
    def evaluate(self, b1, b2, op):
        if op == '&':
            return b1 & b2
        elif op == '|':
            return b1 | b2
        return b1 ^ b2
    
    def countRecur(self, i, j, req, s, memo):
    
        if i == j:
            return 1 if req == (1 if s[i] == 'T' else 0) else 0
    
        if memo[i][j][req] != -1:
            return memo[i][j][req]
    
        ans = 0
        for k in range(i + 1, j, 2):
    
            left_true = self.countRecur(i, k - 1, 1, s, memo)
            left_false = self.countRecur(i, k - 1, 0, s, memo)

            right_true = self.countRecur(k + 1, j, 1, s, memo)
            right_false = self.countRecur(k + 1, j, 0, s, memo)
    
            if self.evaluate(1, 1, s[k]) == req:
                ans += left_true * right_true
            if self.evaluate(1, 0, s[k]) == req:
                ans += left_true * right_false
            if self.evaluate(0, 1, s[k]) == req:
                ans += left_false * right_true
            if self.evaluate(0, 0, s[k]) == req:
                ans += left_false * right_false
    
        memo[i][j][req] = ans
        return ans
        
    def countWays(self, s):
        # code here
        n = len(s)
        memo = [[[-1 for _ in range(2)] for _ in range(n)] for _ in range(n)]
        return self.countRecur(0, n - 1, 1, s, memo)
