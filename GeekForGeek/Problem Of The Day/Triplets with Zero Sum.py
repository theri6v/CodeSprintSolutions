#User function Template for python3
from collections import defaultdict

class Solution:
    def findTriplets(self, arr):
        n = len(arr)
        st = set()  # To store unique triplets
        mp = defaultdict(list)  # Dictionary to store pairs of sums
        
        # Build the map of sum of pairs
        for i in range(n):
            for j in range(i + 1, n):
                mp[arr[i] + arr[j]].append((i, j))
        
        # Now, check for each element if the negative of it exists as a sum in the map
        for i in range(n):
            req = -arr[i]
            if req in mp:
                for pair in mp[req]:
                    if i != pair[0] and i != pair[1]:  # Ensure the indices are distinct
                        curr = [i, pair[0], pair[1]]
                        curr.sort()  # Sort the triplet to ensure i < j < k
                        st.add(tuple(curr))  # Add to set to ensure uniqueness
        
        # Convert set of tuples to a list of lists
        ans = [list(t) for t in st]
        return ans
