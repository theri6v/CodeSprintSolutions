class Solution:
    def getCount(self, n):
        if n == 1:
            return 10
        
        # Transition graph for each digit
        moves = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [2, 1, 3, 5],
            3: [3, 2, 6],
            4: [4, 1, 5, 7],
            5: [5, 2, 4, 6, 8],
            6: [6, 3, 5, 9],
            7: [7, 4, 8],
            8: [8, 5, 7, 9, 0],
            9: [9, 6, 8]
        }
        
        # DP table: dp[length][digit] is the count of sequences of given length ending in the given digit
        dp = [[0] * 10 for _ in range(n + 1)]
        
        # Initial state: sequences of length 1
        for i in range(10):
            dp[1][i] = 1
        
        # Fill the DP table
        for length in range(2, n + 1):
            for digit in range(10):
                dp[length][digit] = sum(dp[length - 1][neighbor] for neighbor in moves[digit])
        
        # Sum up all sequences of length n
        return sum(dp[n][digit] for digit in range(10))
