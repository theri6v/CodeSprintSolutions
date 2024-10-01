# from typing import List

class Solution:
    def rotateDelete(self,  arr):
        n = len(arr)
        for k in range(1, n // 2 + 1):
            arr.insert(0, arr.pop())
            arr.pop(-k)
        return arr[0]
        
