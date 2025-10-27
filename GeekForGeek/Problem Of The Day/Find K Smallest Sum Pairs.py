from heapq import *
class Solution:
    def kSmallestPair(self, arr1, arr2, k):
        m, n = len(arr1), len(arr2)
        heap = []
        ans = []
        for i in range(min(k, m)):
            heappush(heap, (arr1[i] + arr2[0], i, 0))
        while k and heap:
            _, i, j = heappop(heap)
            ans.append((arr1[i], arr2[j]))
            if j + 1 < n:
                heappush(heap, (arr1[i] + arr2[j + 1], i, j + 1))
            k-=1
        return ans
