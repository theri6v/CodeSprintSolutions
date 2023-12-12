# User function Template for Python3

class Solution:
    def maxGold(self, n, m, M):
        # Initialize a 2D array to store the maximum gold values
        dp = [[0] * m for _ in range(n)]

        # Initialize the last column of dp with the values from the mine
        for i in range(n):
            dp[i][m - 1] = M[i][m - 1]

        # Iterate from the second to the first column in reverse order
        for j in range(m - 2, -1, -1):
            for i in range(n):
                # Possible moves: up, right, down
                moves = [i - 1, i, i + 1]

                # Filter out invalid moves
                valid_moves = [move for move in moves if 0 <= move < n]

                # Update dp with the maximum gold value for the current cell
                dp[i][j] = M[i][j] + max(dp[move][j + 1] for move in valid_moves)

        # Find the maximum value in the first column, which represents the starting points
        max_gold = max(dp[i][0] for i in range(n))

        return max_gold
        
