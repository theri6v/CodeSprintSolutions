#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        if n < 4 and n != 1:
            return []
        res = []
        row = [0] * n

        def solve(c, cols, d1, d2):
            if c == n:
                res.append([r + 1 for r in row])
                return
            for r in range(n):
                pos = 1 << r
                if not (cols & pos or d1 & (pos << c) or d2 & (pos << (n - 1 - c))):
                    row[c] = r
                    solve(c + 1, cols | pos, d1 | (pos << c), d2 | (pos << (n - 1 - c)))

        solve(0, 0, 0, 0)
        return res
