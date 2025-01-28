#User function Template for python3

from itertools import permutations

class Solution:
    def findPermutation(self, s):
        return list(set("".join(i) for i in permutations(s)))
        
