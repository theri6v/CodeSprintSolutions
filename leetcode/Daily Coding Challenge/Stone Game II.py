from functools import lru_cache
from itertools import accumulate
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
      
        @lru_cache(maxsize=None)
        def dfs(current_index, max_take):
            # If we can take all remaining piles, return the sum of those piles.
            if max_take * 2 >= total_piles - current_index:
                return prefix_sums[total_piles] - prefix_sums[current_index]
          
            # Try every possible number of stones we can take, and choose the option
            # that maximizes our stones.
            return max(
                prefix_sums[total_piles] - prefix_sums[current_index] - 
                dfs(current_index + x, max(max_take, x))
                for x in range(1, 2 * max_take + 1)
            )

        total_piles = len(piles)  # The total number of piles.
        prefix_sums = list(accumulate(piles, initial=0))  # Prefix sum array to calculate the sum efficiently.     
        # Start the game from the first pile, with the initial maximum of 1 stone to take.
        return dfs(0, 1)
