from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY

        # Use dictionaries to store the disjoint set structure
        parent = {}
        
        # Initialize union-find structure
        for x, y in stones:
            if x not in parent:
                parent[x] = x
            if y + 10001 not in parent:
                parent[y + 10001] = y + 10001
            union(x, y + 10001)
        
        # Find all unique roots
        unique_roots = set(find(x) for x in parent)
        
        # Calculate the number of stones that can be removed
        return len(stones) - len(unique_roots)

# Example usage:
sol = Solution()
print(sol.removeStones([[0,0],[2,2],[10000,2]]))  # Output: 1
