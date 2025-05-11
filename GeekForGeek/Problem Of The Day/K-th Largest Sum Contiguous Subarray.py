from typing import List

from heapq import *

class Solution:
    def kthLargest(self, arr, k) -> int:
        # code here
        min_heap = []
        for i in range(len(arr)):
            summ = 0
            for j in range(i, len(arr)):
                summ += arr[j]
                if len(min_heap) < k:
                    heappush(min_heap, summ)
                else:
                    if min_heap[0] < summ:
                        heappop(min_heap)
                        heappush(min_heap, summ)
        return min_heap[0]
