
from typing import List


class Solution:
    def pairsum(self, arr : List[int]) -> int:
        arr.sort()
        # if len(arr) < 2:
        #     return None
        largest_sum = arr[-1] + arr[-2]
        return largest_sum
