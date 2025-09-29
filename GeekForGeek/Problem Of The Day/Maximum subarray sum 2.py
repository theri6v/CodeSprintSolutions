import heapq

class Solution:
    def maxSubarrSum(self, arr, a, b):
        n = len(arr)
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + arr[i]

        heap = []
        res = float('-inf')

        for r in range(a, n+1):
            heapq.heappush(heap, (prefix[r-a], r-a))
            while heap and heap[0][1] < r-b:
                heapq.heappop(heap)
            res = max(res, prefix[r] - heap[0][0])

        return res
