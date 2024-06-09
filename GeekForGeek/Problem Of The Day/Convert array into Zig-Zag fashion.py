
from typing import List


class Solution:
    def zigZag(self, n : int, arr : List[int]) -> None:
        # code here
        flag = True
        for i in range(n - 1):
            if flag:
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            else:
                if arr[i] < arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            flag = not flag
        return 1
        

