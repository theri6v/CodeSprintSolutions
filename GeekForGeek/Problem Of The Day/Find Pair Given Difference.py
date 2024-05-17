
from typing import List
import math

class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        g={}
        for i in arr:
            if i-x in g or i+x in g:
                return 1
            elif i in g:
                g[i]+=1
            else:
                g[i]=1
        return -1
