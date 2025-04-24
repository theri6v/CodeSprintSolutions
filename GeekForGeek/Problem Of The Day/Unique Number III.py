#User function Template for python3
from collections import defaultdict
class Solution:
    def getSingle(self, arr):
        # code here 
        return (3 * sum(set(arr)) - sum(arr)) // 2
