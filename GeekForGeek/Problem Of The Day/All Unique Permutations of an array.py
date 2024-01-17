#User function Template for python3
from itertools import permutations
class Solution:
    def uniquePerms(self, arr, n):
        unique_perms = set(permutations(arr))
        res = [list(perm) for perm in unique_perms]
        res.sort()
        return res

