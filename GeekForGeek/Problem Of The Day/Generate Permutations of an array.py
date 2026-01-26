from itertools import permutations as pr
class Solution:
    def permuteDist(self, arr):
        # code here
        return list(pr(arr))
