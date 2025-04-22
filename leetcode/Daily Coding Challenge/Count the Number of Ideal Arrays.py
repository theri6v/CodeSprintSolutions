from functools import lru_cache  # Importing lru_cache for caching

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        # Using the lru_cache decorator to memoize the results of the dfs function
        @lru_cache(maxsize=None)
        def dfs(value, length):
            """ 
            Performs a depth-first search starting with a given value
            and length of the sequence, and returns the number of ideal arrays.
            """
            # Initialize result with the combination C(n-1, length-1)
            result = comb_table[-1][length - 1]
            # If we haven't reached the desired length, continue building the sequence
            if length < n:
                multiple = 2
                # Iterate through the possible multiples of 'value' within the maxValue
                while multiple * value <= maxValue:
                    # Recursively call dfs and update the result
                    result = (result + dfs(multiple * value, length + 1)) % MODULE
                    multiple += 1
            return result
      
        # Comb table creation using dynamic programming to calculate combinations
        comb_table = [[0] * 16 for _ in range(n)]
        MODULE = 10**9 + 7  # Module for the problem, to prevent integer overflow
        for i in range(n):
            for j in range(min(16, i + 1)):
                # Base case: There is one way to choose 0 items
                if j == 0:
                    comb_table[i][j] = 1
                else:
                    # Use the recurrence relation C(n, k) = C(n-1, k) + C(n-1, k-1)
                    comb_table[i][j] = (comb_table[i - 1][j] + comb_table[i - 1][j - 1]) % MODULE
      
        # Initial answer is set to zero
        answer = 0
        # Iterate through all possible starting values
        for i in range(1, maxValue + 1):
            # Update the answer by using the dfs function
            answer = (answer + dfs(i, 1)) % MODULE
      
        return answer  # Return the total number of ideal arrays
