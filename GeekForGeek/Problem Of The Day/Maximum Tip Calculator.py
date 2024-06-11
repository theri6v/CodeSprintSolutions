
from typing import List


class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
        # code here
        diff = []
        for i in range(n):
            diff.append((abs(arr[i]-brr[i]), i))
        tip = 0
        diff.sort(reverse=True)
        for i in range(n):
            index = diff[i][1]
            if (arr[index]>brr[index] or y<=0) and x>0:
                tip += arr[index]
                x -= 1
            else:
                tip += brr[index]
                y -= 1
        return tip       
        

